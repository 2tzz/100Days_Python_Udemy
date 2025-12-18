import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2

# Load YOLOv8 model (replace with your road sign model)
model = YOLO("Logs/0day/road_sign.pt")  # trained model for damaged/healthy signs

# Prediction function
def predict_sign_health():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    # Run YOLOv8 inference
    results = model(file_path)
    
    # Read image
    img = cv2.imread(file_path)
    
    detected_labels = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        
        # Define label text based on class
        if cls_id == 0:
            label = f"Damaged ({conf:.2f})"
            color = (0, 0, 255)  # Red for damaged
        else:
            label = f"Healthy ({conf:.2f})"
            color = (0, 255, 0)  # Green for healthy
        
        detected_labels.append(label)
        
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # Convert to ImageTk
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil.thumbnail((500, 500))
    img_tk = ImageTk.PhotoImage(img_pil)
    
    image_label.config(image=img_tk)
    image_label.image = img_tk
    
    if len(detected_labels) > 0:
        result_label.config(text="\n".join(detected_labels), fg="black", font=("Arial", 14))
    else:
        result_label.config(text="No road signs detected", fg="orange", font=("Arial", 14))

# GUI setup
root = tk.Tk()
root.title("Road Sign Damage Detection")
root.geometry("600x600")

Label(root, text="Upload a road sign image", font=("Arial", 14)).pack(pady=10)

btn = tk.Button(root, text="Upload Image", command=predict_sign_health, font=("Arial", 12))
btn.pack(pady=10)

image_label = Label(root)
image_label.pack()

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
