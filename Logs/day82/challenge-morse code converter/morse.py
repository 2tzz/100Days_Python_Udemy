morse_roles = {
    "Q": "––•–",
    "W": "•––",
    "E": "•",
    "R": "•–•",
    "T": "–",
    "Y": "–•––",
    "U": "••–",
    "I": "••",
    "O": "–––",
    "P": "•––•",
    "A": "•–",
    "S": "•••",
    "D": "–••",
    "F": "••–•",
    "G": "––•",
    "H": "••••",
    "J": "•–––",
    "K": "–•–",
    "L": "•–••",
    "Z": "––••",
    "X": "–••–",
    "C": "–•–•",
    "V": "•••–",
    "B": "–•••",
    "N": "–•",
    "M": "––",
    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    "0": "-----",
}
 
 
def turn_into_morse(text):
    output = ""
    try:
        text_input = text.upper().split(" ")
 
        for word in text_input:
            for letter in word:
                output += morse_roles[letter] + " "
    except Exception:
        pass
    return output
 
 
def turn_morse_code_into_text(morse_text: str):
    output = ""
    try:
        text_input = morse_text.split(" ")
        for letter in text_input:
            for key, value in morse_roles.items():
                if value == letter:
                    output += key + " "
    except Exception:
        pass
    return output
 
 
code = turn_into_morse("Hello world this is Suleiman")
decode = turn_morse_code_into_text(code)


