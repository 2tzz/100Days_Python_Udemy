import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2
import numpy as np

# Load YOLOv8 pothole detection model
model = YOLO("Logs/0day/pothol.pt")  # Replace with your pothole model file

def predict_pothole():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    # Run YOLOv8 inference
    results = model(file_path)
    
    # Read original image
    img = cv2.imread(file_path)
    
    # Accuracy info text
    accuracy_texts = []
    
    # Draw results
    for idx, box in enumerate(results[0].boxes, start=1):
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coords
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        
        label = f"Pothole {conf:.2f}"
        color = (0, 0, 255)  # Red for pothole
        
        # Draw rectangle and label on image
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        # Add to accuracy list
        accuracy_texts.append(f"Pothole {idx}: {conf*100:.1f}%")
    
    # Convert to ImageTk for display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil.thumbnail((500, 500))
    img_tk = ImageTk.PhotoImage(img_pil)
    
    image_label.config(image=img_tk)
    image_label.image = img_tk
    
    # Result summary
    if len(results[0].boxes) > 0:
        result_label.config(text=f"🚨 {len(results[0].boxes)} Pothole(s) Detected", fg="red", font=("Arial", 16, "bold"))
        accuracy_box.config(state="normal")
        accuracy_box.delete(1.0, tk.END)
        accuracy_box.insert(tk.END, "\n".join(accuracy_texts))
        accuracy_box.config(state="disabled")
    else:
        result_label.config(text="✅ No Potholes Detected", fg="green", font=("Arial", 16, "bold"))
        accuracy_box.config(state="normal")
        accuracy_box.delete(1.0, tk.END)
        accuracy_box.insert(tk.END, "No detections")
        accuracy_box.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("Pothole Detection")
root.geometry("650x750")

Label(root, text="Upload a road image to check for potholes", font=("Arial", 14)).pack(pady=10)

btn = tk.Button(root, text="Upload Image", command=predict_pothole, font=("Arial", 12))
btn.pack(pady=10)

image_label = Label(root)
image_label.pack()

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Accuracy info box
Label(root, text="Detection Accuracy", font=("Arial", 14, "bold")).pack()
accuracy_box = tk.Text(root, height=6, width=40, font=("Arial", 12))
accuracy_box.pack()
accuracy_box.config(state="disabled")

root.mainloop()
