import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageOps
from io import BytesIO
import os

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking Tool")
        self.root.geometry("1000x600")
        
        # Variables
        self.original_image = None
        self.watermark_image = None
        self.processed_image = None
        self.watermark_position = "bottom-right"  # Default position
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Left Frame - Original Image
        self.left_frame = ttk.LabelFrame(self.root, text="Original Image", width=400, height=500)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.left_frame.grid_propagate(False)
        
        self.original_label = ttk.Label(self.left_frame)
        self.original_label.pack(expand=True)
        
        # Right Frame - Processed Image
        self.right_frame = ttk.LabelFrame(self.root, text="Processed Image", width=400, height=500)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.right_frame.grid_propagate(False)
        
        self.processed_label = ttk.Label(self.right_frame)
        self.processed_label.pack(expand=True)
        
        # Control Frame
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Buttons
        self.upload_btn = ttk.Button(self.control_frame, text="Upload Image", command=self.upload_image)
        self.upload_btn.grid(row=0, column=0, padx=5)
        
        self.remove_btn = ttk.Button(self.control_frame, text="Remove Image", command=self.remove_image)
        self.remove_btn.grid(row=0, column=1, padx=5)
        
        self.watermark_btn = ttk.Button(self.control_frame, text="Upload Watermark", command=self.upload_watermark)
        self.watermark_btn.grid(row=0, column=2, padx=5)
        
        self.position_var = tk.StringVar(value="bottom-right")
        self.position_menu = ttk.OptionMenu(
            self.control_frame, self.position_var, "bottom-right", 
            "top-left", "top-right", "bottom-left", "bottom-right", "center",
            command=self.update_watermark_position
        )
        self.position_menu.grid(row=0, column=3, padx=5)
        
        self.process_btn = ttk.Button(self.control_frame, text="Process Image", command=self.process_image)
        self.process_btn.grid(row=0, column=4, padx=5)
        
        self.download_btn = ttk.Button(self.control_frame, text="Download Image", command=self.download_image)
        self.download_btn.grid(row=0, column=5, padx=5)
        
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
    
    def update_watermark_position(self, position):
        self.watermark_position = position
    
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            try:
                self.original_image = Image.open(file_path)
                self.display_image(self.original_image, self.original_label)
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def remove_image(self):
        self.original_image = None
        self.processed_image = None
        self.original_label.config(image='')
        self.processed_label.config(image='')
    
    def upload_watermark(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.watermark_image = Image.open(file_path)
                # Convert watermark to grayscale (black/white)
                self.watermark_image = ImageOps.grayscale(self.watermark_image)
                tk.messagebox.showinfo("Success", "Watermark uploaded successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to load watermark: {str(e)}")
    
    def process_image(self):
        if not self.original_image:
            tk.messagebox.showerror("Error", "Please upload an image first")
            return
        
        if not self.watermark_image:
            tk.messagebox.showerror("Error", "Please upload a watermark first")
            return
        
        try:
            # Create a copy of the original image
            self.processed_image = self.original_image.copy()
            
            # Resize watermark to be 20% of the original image width
            watermark_width = int(self.original_image.width * 0.2)
            watermark_height = int(self.watermark_image.height * 
                                 (watermark_width / self.watermark_image.width))
            watermark_resized = self.watermark_image.resize(
                (watermark_width, watermark_height), 
                Image.Resampling.LANCZOS
            )
            
            # Convert watermark to RGBA if it's not already
            if watermark_resized.mode != 'RGBA':
                watermark_resized = watermark_resized.convert('RGBA')
            
            # Position the watermark
            if self.watermark_position == "top-left":
                position = (10, 10)
            elif self.watermark_position == "top-right":
                position = (self.original_image.width - watermark_width - 10, 10)
            elif self.watermark_position == "bottom-left":
                position = (10, self.original_image.height - watermark_height - 10)
            elif self.watermark_position == "center":
                position = (
                    (self.original_image.width - watermark_width) // 2,
                    (self.original_image.height - watermark_height) // 2
                )
            else:  # bottom-right (default)
                position = (
                    self.original_image.width - watermark_width - 10,
                    self.original_image.height - watermark_height - 10
                )
            
            # Paste the watermark
            self.processed_image.paste(
                watermark_resized, 
                position, 
                watermark_resized
            )
            
            # Display the processed image
            self.display_image(self.processed_image, self.processed_label)
            
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to process image: {str(e)}")
    
    def display_image(self, image, label):
        # Resize image to fit in the frame while maintaining aspect ratio
        max_width = 380
        max_height = 450
        
        width, height = image.size
        ratio = min(max_width/width, max_height/height)
        new_size = (int(width * ratio), int(height * ratio))
        resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(resized_image)
        
        # Update the label
        label.config(image=photo)
        label.image = photo  # Keep a reference
    
    def download_image(self):
        if not self.processed_image:
            tk.messagebox.showerror("Error", "No processed image to download")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.processed_image.save(file_path)
                tk.messagebox.showinfo("Success", "Image saved successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to save image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()