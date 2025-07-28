import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

class MorseCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")
        
        # Morse code dictionary
        self.morse_roles = {
            "Q": "––•–", "W": "•––", "E": "•", "R": "•–•", "T": "–", 
            "Y": "–•––", "U": "••–", "I": "••", "O": "–––", "P": "•––•", 
            "A": "•–", "S": "•••", "D": "–••", "F": "••–•", "G": "––•", 
            "H": "••••", "J": "•–––", "K": "–•–", "L": "•–••", "Z": "––••", 
            "X": "–••–", "C": "–•–•", "V": "•••–", "B": "–•••", "N": "–•", 
            "M": "––", "1": "•----", "2": "••---", "3": "•••--", 
            "4": "••••-", "5": "•••••", "6": "-••••", "7": "--•••", 
            "8": "---••", "9": "----•", "0": "-----", " ": "/"
        }
        
        # Reverse dictionary for decoding
        self.reverse_morse = {v: k for k, v in self.morse_roles.items()}
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Custom font
        custom_font = ("Segoe UI", 10)
        title_font = ("Segoe UI", 16, "bold")
        
        # Header frame
        header_frame = tk.Frame(self.root, bg="#2c3e50")
        header_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            header_frame, 
            text="Morse Code Translator", 
            font=title_font, 
            fg="white", 
            bg="#2c3e50"
        ).pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#808080")
        input_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        tk.Label(
            input_frame, 
            text="Enter text to encode or Morse code to decode:", 
            font=custom_font, 
            bg="#FFFCFC"
        ).pack(anchor="w", pady=(0, 5))
        
        self.input_text = ScrolledText(
            input_frame, 
            height=8, 
            font=custom_font, 
            wrap=tk.WORD, 
            padx=10, 
            pady=10,
            bg="white",
            relief=tk.FLAT
        )
        self.input_text.pack(fill="both", expand=True)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#808080")
        button_frame.pack(fill="x", padx=20, pady=10)
        
        style = ttk.Style()
        style.configure("TButton", font=custom_font, padding=6)
        style.map("TButton", 
                  foreground=[('pressed', 'white'), ('active', 'white')],
                  background=[('pressed', '#16a085'), ('active', '#1abc9c')])
        
        ttk.Button(
            button_frame, 
            text="Encode to Morse", 
            command=self.encode_to_morse,
            style="TButton"
        ).pack(side="left", padx=5, pady=5, ipadx=10)
        
        ttk.Button(
            button_frame, 
            text="Decode to Text", 
            command=self.decode_to_text,
            style="TButton"
        ).pack(side="left", padx=5, pady=5, ipadx=10)
        
        ttk.Button(
            button_frame, 
            text="Clear All", 
            command=self.clear_all,
            style="TButton"
        ).pack(side="right", padx=5, pady=5, ipadx=10)
        
        # Output frame
        output_frame = tk.Frame(self.root, bg="#f5f5f5")
        output_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        tk.Label(
            output_frame, 
            text="Result:", 
            font=custom_font, 
            bg="#f5f5f5"
        ).pack(anchor="w", pady=(0, 5))
        
        self.output_text = ScrolledText(
            output_frame, 
            height=8, 
            font=custom_font, 
            wrap=tk.WORD, 
            padx=10, 
            pady=10,
            bg="white",
            relief=tk.FLAT,
            state="disabled"
        )
        self.output_text.pack(fill="both", expand=True)
    
    def encode_to_morse(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to encode")
            return
        
        try:
            output = ""
            text_input = text.upper().split(" ")
            
            for word in text_input:
                for letter in word:
                    if letter in self.morse_roles:
                        output += self.morse_roles[letter] + " "
                    else:
                        output += letter + " "  # Keep unsupported characters as-is
                output += "/ "
            
            self.display_output(output.strip())
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during encoding: {str(e)}")
    
    def decode_to_text(self):
        morse_text = self.input_text.get("1.0", tk.END).strip()
        if not morse_text:
            messagebox.showwarning("Warning", "Please enter some Morse code to decode")
            return
        
        try:
            output = ""
            text_input = morse_text.split(" ")
            
            for code in text_input:
                if code in self.reverse_morse:
                    output += self.reverse_morse[code]
                elif code == "/":
                    output += " "
                else:
                    output += code  # Keep unrecognized codes as-is
            
            self.display_output(output)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during decoding: {str(e)}")
    
    def display_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)
        self.output_text.config(state="disabled")
    
    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeApp(root)
    root.mainloop()