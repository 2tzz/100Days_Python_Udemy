# Image Processing Project

This project is a Python-based image processing application that provides various tools for manipulating and analyzing images. Below is an overview of the technologies used and the functionality provided by the project.

## Technologies Used

- **Python** - The core programming language used for the project
- **OpenCV (cv2)** - For computer vision and image processing tasks
- **NumPy** - For numerical operations on image data
- **Matplotlib** - For displaying and visualizing images
- **Pillow (PIL)** - For basic image operations and file handling
- **scikit-image** - For advanced image processing algorithms
- **PyQt5** - For the graphical user interface (GUI)

## Features

### 1. Basic Image Operations

```python
import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the processed image
cv2.imwrite('gray_image.jpg', gray_image)
```

### 2. Edge Detection

```python
# Canny edge detection
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Display edges
cv2.imshow('Edges', edges)
cv2.waitKey(0)
```

### 3. Image Filtering

```python
# Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Median blur
median = cv2.medianBlur(image, 5)
```

### 4. Thresholding

```python
# Binary thresholding
_, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(
    gray_image, 255, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY, 11, 2
)
```

### 5. Contour Detection

```python
# Find contours
contours, _ = cv2.findContours(
    edges, 
    cv2.RETR_TREE, 
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw contours
contour_image = cv2.drawContours(
    image.copy(), 
    contours, 
    -1, (0, 255, 0), 2
)
```

### 6. Histogram Equalization

```python
# Equalize histogram
equalized = cv2.equalizeHist(gray_image)

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(gray_image)
```

### 7. Feature Detection

```python
# ORB feature detector
orb = cv2.ORB_create()
keypoints, descriptors = orb.detectAndCompute(gray_image, None)

# Draw keypoints
keypoint_image = cv2.drawKeypoints(
    image, 
    keypoints, 
    None, 
    color=(0, 255, 0), 
    flags=0
)
```

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/2tzz/Image-Processing-Project.git
   cd Image-Processing-Project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main application:
   ```bash
   python main.py
   ```

4. Use the GUI to load images and apply various processing techniques.

