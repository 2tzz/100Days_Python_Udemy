# Day 27 - Python Exercises_

Welcome to **Day 27** of the **100 Days of Python** challenge! 🎯 This day focuses on Object-Oriented Programming (OOP) in Python, with exercises aimed at strengthening your understanding of classes, objects, and Tkinter for GUI development.

## 🚀 Topics Covered
- Object-Oriented Programming (OOP)
- Creating and using classes
- Working with Tkinter to build graphical applications
- Creating and using class methods and instance methods
- Understanding `args` and `kwargs` in function calls

## 📝 Exercises Completed

### 1️⃣ **Creating a Simple Class**
- Defined a `Car` class with attributes like `brand`, `model`, and `year`.
- Created instances of the class and printed attributes.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

my_car = Car("Toyota", "Corolla", 2022)
print(my_car.display_info())
```

### 2️⃣ **Using `@classmethod` and `@staticmethod`**
- Created a `Student` class with methods for displaying student details.
- Implemented class methods for alternative constructors.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, student_str):
        name, age = student_str.split(",")
        return cls(name, int(age))
    
    def display_info(self):
        return f"Student: {self.name}, Age: {self.age}"

student1 = Student.from_string("Alice,21")
print(student1.display_info())
```

### 3️⃣ **GUI Application with Tkinter**
- Built a simple GUI using Tkinter.
- Created buttons, labels, and text input fields.
- Implemented event handling for button clicks.

```python
import tkinter as tk

def on_button_click():
    label.config(text=f"Hello, {entry.get()}!")

root = tk.Tk()
root.title("Simple Tkinter App")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

root.mainloop()
```

### 4️⃣ **Understanding `*args` and `**kwargs`**
- Created functions that accept variable-length arguments.
- Demonstrated the use of `*args` for summing numbers.
- Used `**kwargs` to format and display keyword arguments dynamically.

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="John", age=30, city="New York")
```

## 📂 File Structure
```
📁 day27
 ┣ 📜 main.py   # Contains the primary Python script with exercises
 ┣ 📜 tkinter_app.py  # A simple Tkinter-based GUI application
 ┗ 📜 README.md  # This file
```

## 🏆 Key Takeaways
- OOP makes Python programs more modular and reusable.
- Tkinter is a powerful built-in library for creating GUI applications.
- `*args` allows passing multiple positional arguments, while `**kwargs` allows passing multiple keyword arguments.

## 🎯 Next Steps
- Continue practicing OOP by creating more complex classes.
- Experiment with Tkinter to develop interactive applications.
- Explore Python decorators and their practical use cases.

Happy coding! 🚀

