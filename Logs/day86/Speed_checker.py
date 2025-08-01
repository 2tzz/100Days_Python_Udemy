import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        
        # Sample texts for typing test
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog. This sentence contains all the letters in the English alphabet.",
            "Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
            "To be or not to be, that is the question. Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune.",
            "The journey of a thousand miles begins with a single step. You must be the change you wish to see in the world.",
            "Python is an interpreted, high-level, general-purpose programming language. Its design philosophy emphasizes code readability."
        ]
        
        # High scores storage
        self.high_scores = []
        
        # Test variables
        self.test_active = False
        self.start_time = 0
        self.current_text = ""
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        self.title_label = ttk.Label(
            self.main_frame, 
            text="Typing Speed Test", 
            font=("Helvetica", 18, "bold")
        )
        self.title_label.pack(pady=10)
        
        # Instructions
        self.instructions = ttk.Label(
            self.main_frame,
            text="Type the text below as quickly and accurately as possible.\nPress Start to begin the test.",
            wraplength=600,
            justify=tk.CENTER
        )
        self.instructions.pack(pady=10)
        
        # Sample text display
        self.sample_text_frame = ttk.LabelFrame(self.main_frame, text="Text to Type", padding=10)
        self.sample_text_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.sample_text = tk.Text(
            self.sample_text_frame,
            height=6,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.sample_text.pack(fill=tk.BOTH, expand=True)
        
        # User input
        self.user_input_frame = ttk.LabelFrame(self.main_frame, text="Your Typing", padding=10)
        self.user_input_frame.pack(fill=tk.BOTH, pady=10)
        
        self.user_input = tk.Text(
            self.user_input_frame,
            height=6,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            padx=10,
            pady=10
        )
        self.user_input.pack(fill=tk.BOTH, expand=True)
        self.user_input.bind("<Key>", self.check_start)
        
        # Results frame
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Results", padding=10)
        self.results_frame.pack(fill=tk.BOTH, pady=10)
        
        self.results_text = tk.Text(
            self.results_frame,
            height=4,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Control buttons
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.pack(pady=10)
        
        self.start_button = ttk.Button(
            self.controls_frame,
            text="Start Test",
            command=self.start_test
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = ttk.Button(
            self.controls_frame,
            text="Reset",
            command=self.reset_test
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # High scores button
        self.high_scores_button = ttk.Button(
            self.controls_frame,
            text="View High Scores",
            command=self.show_high_scores
        )
        self.high_scores_button.pack(side=tk.LEFT, padx=5)
        
        # Set initial state
        self.reset_test()
    
    def start_test(self):
        """Start a new typing test"""
        if not self.test_active:
            self.test_active = True
            self.start_time = time.time()
            self.current_text = random.choice(self.sample_texts)
            
            # Update UI
            self.sample_text.config(state=tk.NORMAL)
            self.sample_text.delete(1.0, tk.END)
            self.sample_text.insert(tk.END, self.current_text)
            self.sample_text.config(state=tk.DISABLED)
            
            self.user_input.delete(1.0, tk.END)
            self.user_input.focus()
            
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Test in progress...")
            self.results_text.config(state=tk.DISABLED)
            
            self.start_button.config(text="Test Running...", state=tk.DISABLED)
    
    def check_start(self, event):
        """Check if user started typing to begin timing"""
        if not self.test_active and self.user_input.get(1.0, "end-1c"):
            self.start_test()
    
    def reset_test(self):
        """Reset the typing test"""
        self.test_active = False
        self.start_time = 0
        self.current_text = ""
        
        # Update UI
        self.sample_text.config(state=tk.NORMAL)
        self.sample_text.delete(1.0, tk.END)
        self.sample_text.insert(tk.END, "Press Start to begin a new test.")
        self.sample_text.config(state=tk.DISABLED)
        
        self.user_input.delete(1.0, tk.END)
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "Results will appear here after completing a test.")
        self.results_text.config(state=tk.DISABLED)
        
        self.start_button.config(text="Start Test", state=tk.NORMAL)
    
    def calculate_results(self):
        """Calculate and display typing speed results"""
        if not self.test_active:
            return
        
        end_time = time.time()
        time_taken = end_time - self.start_time
        minutes = time_taken / 60
        
        typed_text = self.user_input.get(1.0, tk.END).strip()
        original_words = self.current_text.split()
        typed_words = typed_text.split()
        
        # Calculate words per minute
        word_count = len(typed_words)
        wpm = int(word_count / minutes) if minutes > 0 else 0
        
        # Calculate accuracy
        correct_chars = 0
        min_length = min(len(self.current_text), len(typed_text))
        
        for i in range(min_length):
            if self.current_text[i] == typed_text[i]:
                correct_chars += 1
        
        accuracy = (correct_chars / len(self.current_text)) * 100 if len(self.current_text) > 0 else 0
        
        # Save to high scores
        self.high_scores.append({
            "wpm": wpm,
            "accuracy": accuracy,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        # Keep only top 10 scores
        self.high_scores = sorted(self.high_scores, key=lambda x: x["wpm"], reverse=True)[:10]
        
        # Display results
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        
        result_message = (
            f"Typing Speed: {wpm} WPM\n"
            f"Accuracy: {accuracy:.2f}%\n"
            f"Time Taken: {time_taken:.2f} seconds\n"
            f"Words Typed: {word_count}"
        )
        
        # Add feedback based on WPM
        if wpm < 30:
            result_message += "\n\nKeep practicing! Average is 40 WPM."
        elif wpm < 60:
            result_message += "\n\nGood! You're above average."
        elif wpm < 100:
            result_message += "\n\nExcellent! You're a fast typist."
        else:
            result_message += "\n\nAmazing! You're a typing pro!"
        
        self.results_text.insert(tk.END, result_message)
        self.results_text.config(state=tk.DISABLED)
        
        self.test_active = False
        self.start_button.config(text="Start New Test", state=tk.NORMAL)
    
    def show_high_scores(self):
        """Display high scores in a new window"""
        high_scores_window = tk.Toplevel(self.root)
        high_scores_window.title("High Scores")
        high_scores_window.geometry("400x300")
        
        title_label = ttk.Label(
            high_scores_window,
            text="Top Typing Scores",
            font=("Helvetica", 14, "bold")
        )
        title_label.pack(pady=10)
        
        if not self.high_scores:
            no_scores = ttk.Label(
                high_scores_window,
                text="No high scores yet! Complete a test to see your results.",
                wraplength=350,
                justify=tk.CENTER
            )
            no_scores.pack(pady=20)
        else:
            scores_frame = ttk.Frame(high_scores_window)
            scores_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            
            # Header
            ttk.Label(scores_frame, text="Rank", font=("Helvetica", 10, "bold")).grid(row=0, column=0, padx=5, pady=2)
            ttk.Label(scores_frame, text="WPM", font=("Helvetica", 10, "bold")).grid(row=0, column=1, padx=5, pady=2)
            ttk.Label(scores_frame, text="Accuracy", font=("Helvetica", 10, "bold")).grid(row=0, column=2, padx=5, pady=2)
            ttk.Label(scores_frame, text="Date", font=("Helvetica", 10, "bold")).grid(row=0, column=3, padx=5, pady=2)
            
            # Scores
            for i, score in enumerate(self.high_scores, 1):
                ttk.Label(scores_frame, text=f"{i}.").grid(row=i, column=0, padx=5, pady=2)
                ttk.Label(scores_frame, text=f"{score['wpm']}").grid(row=i, column=1, padx=5, pady=2)
                ttk.Label(scores_frame, text=f"{score['accuracy']:.2f}%").grid(row=i, column=2, padx=5, pady=2)
                ttk.Label(scores_frame, text=score['time']).grid(row=i, column=3, padx=5, pady=2)
        
        close_button = ttk.Button(
            high_scores_window,
            text="Close",
            command=high_scores_window.destroy
        )
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    
    # Bind Enter key to calculate results
    root.bind("<Return>", lambda e: app.calculate_results())
    
    root.mainloop()