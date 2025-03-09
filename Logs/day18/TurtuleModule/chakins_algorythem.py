from turtle import Turtle, Screen

# Function to apply Chaikin's algorithm
def chaikin_smoothing(points, iterations=1):
    for _ in range(iterations):
        new_points = []
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            q = (0.75 * p1[0] + 0.25 * p2[0], 0.75 * p1[1] + 0.25 * p2[1])
            r = (0.25 * p1[0] + 0.75 * p2[0], 0.25 * p1[1] + 0.75 * p2[1])
            new_points.extend([q, r])
        points = new_points
    return points

# Function to draw a polygon
def draw_polygon(turtle, points, color):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.color(color)
    
    for point in points:
        turtle.goto(point)
    turtle.goto(points[0])  # Close the polygon
    

# Initialize Turtle
timmy = Turtle()
timmy.shape("circle")
timmy.shapesize(1, 1)
timmy.speed(10)

# Define initial polygon (square)
initial_points = [(-200, -200), (200, -200), (200, 200), (-200, 200)]

# Apply Chaikin's algorithm and visualize step by step
for iteration in range(4):
    smoothed_points = chaikin_smoothing(initial_points, iterations=iteration)
    draw_polygon(timmy, smoothed_points, "blue")
    initial_points = smoothed_points  # Update for next iteration

# Set up the screen
screen = Screen()
screen.exitonclick()