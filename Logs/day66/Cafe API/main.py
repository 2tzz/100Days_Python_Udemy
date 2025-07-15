from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from sqlalchemy.exc import IntegrityError

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():  # Renamed from GET() to follow Python naming conventions
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    
    # Return the random cafe's data as JSON
    return jsonify(
        id=random_cafe.id,
        name=random_cafe.name,
        map_url=random_cafe.map_url,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        seats=random_cafe.seats,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        has_sockets=random_cafe.has_sockets,
        can_take_calls=random_cafe.can_take_calls,
        coffee_price=random_cafe.coffee_price
    )
 

@app.route("/all")
def get_all_cafes():
    all_cafes = Cafe.query.all()
    cafes_list = []
    
    for cafe in all_cafes:  # Only one loop needed
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        cafes_list.append(cafe_dict)
    
    return jsonify(cafes=cafes_list)        

@app.route("/search")
def search_cafes():
    # Get the 'loc' parameter from the URL (e.g., /search?loc=London)
    user_loc = request.args.get("loc")
    
    if not user_loc:
        return jsonify(
            error={"Bad Request": "Please provide a 'loc' parameter in the URL."}
        ), 400
    
    # Filter cafes by location (case-insensitive)
    matching_cafes = Cafe.query.filter(Cafe.location.ilike(f"%{user_loc}%")).all()
    
    if not matching_cafes:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."}
        ), 404
    
  
    cafes_list = [
        {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        for cafe in matching_cafes
    ]
    
    return jsonify(cafes=cafes_list)


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    # Get data from the POST request (form data or JSON)
    data = request.form if request.form else request.get_json()

    # Validate required fields
    required_fields = [
        "name", "map_url", "img_url", "location", "seats",
        "has_toilet", "has_wifi", "has_sockets", "can_take_calls"
    ]
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify(
            error={"Missing Fields": f"Required fields: {', '.join(missing_fields)}"}
        ), 400

    # Create a new Cafe record
    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=bool(data["has_toilet"]),
        has_wifi=bool(data["has_wifi"]),
        has_sockets=bool(data["has_sockets"]),
        can_take_calls=bool(data["can_take_calls"]),
        coffee_price=data["coffee_price"]
    )

    # Add to database
    db.session.add(new_cafe)
    db.session.commit()

    # Return success response
    return jsonify(
        success={"message": "Cafe added successfully!", "id": new_cafe.id}
    ), 201

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    # Try to get new_price from all possible sources
    new_price = (
        request.args.get("new_price") or  # URL query parameters (e.g., ?new_price=$5.00)
        (request.json.get("new_price") if request.is_json else None) or  # JSON body
        request.form.get("new_price")  # Form data
    )

    # Validate new_price exists
    if not new_price:
        return jsonify(
            error={
                "Missing Field": "Please provide 'new_price' as: "
                "(1) URL parameter (?new_price=...), "
                "(2) JSON body, or "
                "(3) form data."
            }
        ), 400

    if not isinstance(new_price, str) or len(new_price.strip()) == 0:
        return jsonify(
            error={"Invalid Price": "Price must be a non-empty string"}
        ), 400

    # Get cafe from database
    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(
            error={"Not Found": f"Sorry, a cafe with id {cafe_id} was not found."}
        ), 404

    # Update and commit
    try:
        cafe.coffee_price = new_price.strip()
        db.session.commit()
        return jsonify(
            success={
                "message": f"Successfully updated price to {new_price}",
                "cafe": {
                    "id": cafe.id,
                    "name": cafe.name,
                    "new_price": cafe.coffee_price
                }
            }
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            error={
                "Database Error": "Failed to update price",
                "details": str(e)
            }
        ), 500


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE", "OPTIONS"])
def delete_cafe(cafe_id):
    print("\n=== Received Headers ===")
    for k, v in request.headers.items():
        print(f"{k}: {v}")
    
    api_key = (
        request.headers.get("X-API-Key") or 
        request.headers.get("x-api-key") or
        request.headers.get("Api-Key")
    )
    print(f"Extracted API Key: {api_key}")
    
    if not api_key:
        return jsonify(error={"Unauthorized": "API key is missing"}), 403
    if api_key != "alwisXYZ@123":
        return jsonify(error={"Forbidden": "Invalid API key"}), 403
    
    # Find the cafe
    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": f"Cafe with id {cafe_id} not found"}), 404
    
    # Delete the cafe
    try:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(
            success={"message": f"Successfully deleted cafe {cafe_id}: {cafe.name}"}
        ), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(
            error={"Database Error": f"Failed to delete cafe: {str(e)}"}
        ), 500

if __name__ == '__main__':
    app.run(debug=True)
