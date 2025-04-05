# Day 34 - Python Udemy 100 Days Challenge

## Project: Quizzler App (GUI Quiz Game)
This project builds a quiz game application using the Open Trivia Database API and Python's Tkinter library. The user answers multiple choice questions presented through a simple and responsive graphical user interface.

## What It Does
- Fetches trivia questions dynamically from an online API.
- Displays one question at a time in a GUI.
- Lets users answer with "True" or "False" buttons.
- Tracks the score based on correct answers.
- Ends the quiz once all questions are answered.

## Features
- API-based trivia quiz content
- Graphical User Interface using Tkinter
- Score tracking and live updates
- Interactive feedback after each answer (right or wrong)

## Concepts Practiced
- API integration
- Working with JSON data
- Tkinter GUI components: Labels, Buttons, Canvas
- Object-Oriented Programming (OOP)
- Custom classes and method interaction

## File Structure
```
day34/
├── main.py              # Entry point with GUI setup
├── quiz_brain.py        # Handles quiz logic and question validation
├── question_model.py    # Data model for questions
├── data.py              # API interaction and question list building
├── ui.py                # UI class for interface rendering
├── README.md            # Project documentation
```

## How It Works
1. **Fetches Questions**
   ```python
   response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
   question_data = response.json()["results"]
   ```
2. **Displays Questions in GUI**
   ```python
   self.canvas.itemconfig(self.question_text, text=q_text)
   ```
3. **Handles User Input and Feedback**
   ```python
   def true_pressed(self):
       is_right = self.quiz.check_answer("True")
       self.give_feedback(is_right)
   ```

## How to Run
### Requirements
- Python 3
- Modules: `requests`, `tkinter`

### Steps
```bash
python main.py
```
Make sure you are connected to the internet to fetch trivia data from the API.

## Summary
This is a well-rounded project that brings together API consumption, GUI programming, and structured logic. It offers a solid foundation for building more complex quiz-based or learning applications.

---
Let me know if you’d like to add categories, timer features, or save user scores! :)