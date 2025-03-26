# Day 31 - Python Udemy 100 Days Challenge

## Overview
This project is part of the **100 Days of Python Udemy Course**, specifically focusing on **Day 31**. The challenge explores **Flash Card Applications**, where users can review and memorize words using an interactive GUI.

## Key Features
- **Tkinter GUI** for an interactive flash card system.
- **CSV to Dictionary Conversion** for managing word data.
- **Auto-Flipping Cards** after a set time interval.
- **Saving Progress** by tracking learned words.

## Code Snippets & Highlights

### **1. Loading Data from CSV into a Dictionary**
This code reads a CSV file and converts it into a list of dictionaries for easy access.
```python
import pandas as pd

try:
    data = pd.read_csv("data/french_words.csv")
    word_dict = data.to_dict(orient="records")
except FileNotFoundError:
    print("File not found!")
```
✅ *Handles file errors gracefully and converts CSV data into a structured dictionary.*

### **2. Auto-Flip Mechanism Using `after()`**
This function flips the card after 3 seconds to reveal the translation.
```python
import tkinter as tk

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")

window.after(3000, flip_card)  # Auto flip after 3 seconds
```
✅ *Creates a delay before flipping the card, improving the memorization process.*

### **3. Removing Learned Words and Updating Data**
Users can mark words as known, and the program removes them from future reviews.
```python
word_dict.remove(current_card)
new_data = pd.DataFrame(word_dict)
new_data.to_csv("data/words_to_learn.csv", index=False)
```
✅ *Ensures progress tracking by saving unlearned words for later practice.*

## Installation & Setup

### **Prerequisites**
Ensure you have the following installed before running the project:
- **Python 3.x**
- **Tkinter** (included with most Python installations)
- **Pandas** for data manipulation:
  ```sh
  pip install pandas
  ```

### **Steps to Run the Project**
1. **Clone the Repository**
   ```sh
   git clone https://github.com/2tzz/100Days_Python_Udemy.git
   cd 100Days_Python_Udemy/Logs/day31
   ```

2. **Run the Python Script**
   ```sh
   python main.py
   ```

## File Structure
```
Logs/day31/
│── main.py          # Main Python script for flash card app
│── data/french_words.csv # Word data for flash cards
│── README.md        # Documentation for the project
```

## Usage
- Run the script to launch the flash card application.
- Flip between words to memorize them.
- Mark words as "Known" to remove them from future sessions.

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your fork and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, please open an issue on the GitHub repository.

---

Let me know if you need any modifications! 🚀

