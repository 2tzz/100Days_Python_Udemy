import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO
import os

class RoadDamageDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Road Damage Detection")
        self.root.geometry("1200x800")
        
        # Load the trained model
        self.model = YOLO('Logs/0day/road_damage.pt')  # Update path if needed
        
        # Damage class names
        self.class_names = ['D00', 'D10', 'D20', 'D40', 'D43', 'D44', 'D50']
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Frame for image display
        self.image_frame = tk.Frame(self.root, width=800, height=600, bg='white')
        self.image_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Frame for controls
        self.control_frame = tk.Frame(self.root, width=300, height=600, bg='lightgray')
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)
        
        # Image label
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        self.load_btn = tk.Button(self.control_frame, text="Load Image", command=self.load_image)
        self.load_btn.pack(pady=10, fill=tk.X)
        
        self.detect_btn = tk.Button(self.control_frame, text="Detect Damage", command=self.detect_damage)
        self.detect_btn.pack(pady=10, fill=tk.X)
        
        self.camera_btn = tk.Button(self.control_frame, text="Use Camera", command=self.use_camera)
        self.camera_btn.pack(pady=10, fill=tk.X)
        
        self.save_btn = tk.Button(self.control_frame, text="Save Results", command=self.save_results)
        self.save_btn.pack(pady=10, fill=tk.X)
        
        # Damage info display
        self.info_label = tk.Label(self.control_frame, text="Damage Information:", bg='lightgray')
        self.info_label.pack(pady=10, fill=tk.X)
        
        self.damage_text = tk.Text(self.control_frame, height=15, width=30)
        self.damage_text.pack(pady=10, fill=tk.X)
        self.damage_text.config(state=tk.DISABLED)
        
        # Current image path
        self.current_image_path = None
        self.current_image = None
        self.processed_image = None
        
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )
        
        if file_path:
            self.current_image_path = file_path
            self.display_image(file_path)
            
    def display_image(self, image_path):
        try:
            image = Image.open(image_path)
            # Resize to fit the window
            image.thumbnail((800, 600))
            photo = ImageTk.PhotoImage(image)
            
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference
            self.current_image = image
            
            # Clear previous detection results
            self.processed_image = None
            self.update_damage_info([])
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def detect_damage(self):
        if not self.current_image_path:
            messagebox.showwarning("Warning", "Please load an image first")
            return
            
        try:
            # Run detection
            results = self.model(self.current_image_path)
            
            # Get the first result (since we're processing one image)
            result = results[0]
            
            # Get the annotated image
            annotated_image = result.plot()  # Returns a BGR numpy array
            
            # Convert to RGB for display
            annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
            self.processed_image = Image.fromarray(annotated_image)
            
            # Display the annotated image
            display_image = self.processed_image.copy()
            display_image.thumbnail((800, 600))
            photo = ImageTk.PhotoImage(display_image)
            
            self.image_label.config(image=photo)
            self.image_label.image = photo
            
            # Extract detection information
            detections = []
            for box in result.boxes:
                class_id = int(box.cls)
                confidence = float(box.conf)
                bbox = box.xyxy[0].tolist()
                
                detections.append({
                    'class': self.class_names[class_id],
                    'confidence': confidence,
                    'bbox': bbox
                })
            
            # Update damage information
            self.update_damage_info(detections)
            
        except Exception as e:
            messagebox.showerror("Error", f"Detection failed: {str(e)}")
    
    def update_damage_info(self, detections):
        self.damage_text.config(state=tk.NORMAL)
        self.damage_text.delete(1.0, tk.END)
        
        if not detections:
            self.damage_text.insert(tk.END, "No damages detected")
        else:
            for i, detection in enumerate(detections, 1):
                self.damage_text.insert(tk.END, 
                    f"Damage {i}:\n"
                    f"Type: {detection['class']}\n"
                    f"Confidence: {detection['confidence']:.2f}\n"
                    f"Location: {detection['bbox']}\n\n"
                )
        
        self.damage_text.config(state=tk.DISABLED)
    
    def use_camera(self):
        messagebox.showinfo("Info", "Camera functionality would be implemented here")
        # You would add code to capture from webcam and process frames
    
    def save_results(self):
        if not self.processed_image:
            messagebox.showwarning("Warning", "No detection results to save")
            return
            
        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")]
        )
        
        if save_path:
            try:
                self.processed_image.save(save_path)
                messagebox.showinfo("Success", "Results saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RoadDamageDetector(root)
    root.mainloop()