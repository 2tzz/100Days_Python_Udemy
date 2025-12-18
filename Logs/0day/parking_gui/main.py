import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("Logs/0day/parking.pt")  # your trained weights

# Prediction function
def predict_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    # Run YOLO prediction
    results = model(file_path)
    
    # Read image with OpenCV
    img = cv2.imread(file_path)
    
    # Draw bounding boxes and labels
    preds = results[0].boxes
    detected_classes = preds.cls.cpu().numpy()
    detected_conf = preds.conf.cpu().numpy()
    
    for box, cls_id, conf in zip(preds.xyxy.cpu().numpy(), detected_classes, detected_conf):
        x1, y1, x2, y2 = map(int, box)
        label = f"{'Illegal' if cls_id == 0 else 'Legal'} {conf*100:.1f}%"
        color = (0, 0, 255) if cls_id == 0 else (0, 255, 0)
        
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    
    # Convert OpenCV image to Tkinter
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil.thumbnail((400, 400))
    img_tk = ImageTk.PhotoImage(img_pil)
    
    image_label.config(image=img_tk)
    image_label.image = img_tk
    
    # Decide legality based on detections
    if len(detected_classes) > 0:
        if any(cls_id == 0 for cls_id in detected_classes):
            result_label.config(text="🚫 Illegal Parking", fg="red", font=("Arial", 16, "bold"))
        else:
            result_label.config(text="✅ Legal Parking", fg="green", font=("Arial", 16, "bold"))
    else:
        result_label.config(text="No cars detected", fg="orange", font=("Arial", 16, "bold"))

# GUI setup
root = tk.Tk()
root.title("Parking Detection")
root.geometry("500x550")

Label(root, text="Upload a parking image to check legality", font=("Arial", 14)).pack(pady=10)

btn = tk.Button(root, text="Upload Image", command=predict_image, font=("Arial", 12))
btn.pack(pady=10)

image_label = Label(root)
image_label.pack()

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
