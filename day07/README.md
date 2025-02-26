# Day 7 - Hangman

![](hangman.gif)




## Exercises
### Excercise 1 - Picking a Random Words and Checking Answers
**Instructions:**
- Randomly choose a word from the word_list and assign it to a variable called chosen_word.
- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
- Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


**Code**
<details><summary>Solution</summary>
<p>

```Python
import random

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
```

</p>
</details>

#

### Excercise 2 - Replacing Blanks With Guesses
**Instructions:**
- Create an empty List called display.
- For each letter in the chosen_word, add a "_" to 'display'.
- So if the chosen_word was "apple", display should be `["_", "_", "_", "_", "_"]` with 5 "_" representing each letter to guess. 

- Loop through each position in the chosen_word.
- If the letter at that position matches 'guess' then reveal that letter in the display at that position.
- E.g. If the user guessed "p" and the chosen word was "apple", then display should be `["_", "p", "p", "_", "_"]`.

- Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

**Code**
<details><summary>Solution</summary>
<p>

```Python
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
  display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter
print(display)
```

</p>
</details>

#

### Excercise 3 - Checking if the Player Has Won 
**Instructions:**
- Use a while loop to let the user guess again. 
- The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
- Then you can tell the user they've won.

**Code**
<details><summary>Solution</summary>
<p>

```Python
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
  display += "_"

end_of_game = False

while end_of_game != True:
  guess = input("Guess a letter: ").lower()
  for position in range(word_length):
      letter = chosen_word[position]
      print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter
      
  print(display)

  if "_" not in display:
    end_of_game = True
    print("You Win!")
```

</p>
</details>

#

### Excercise 4 - Keeping Track of the Player's Lives
**Instructions:**
- Create a variable called 'lives' to keep track of the number of lives left. 
- Set 'lives' to equal 6.
- If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
- If lives goes down to 0 then the game should stop and it should print "You lose."
- Join all the elements in the list and turn it into a String.
- Check if user has got all letters.
- print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

**Code**
<details><summary>Solution</summary>
<p>

```Python
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
      end_of_game = True
      print("You win.")

  print(stages[lives])
```

</p>
</details>

#

### Excercise 5 - Improving the User Experience
**Instructions:**
- Update the word list to use the 'word_list' from hangman_words.py
- Delete line: `word_list = ["ardvark", "baboon", "camel"]`
- Import the logo from hangman_art.py and print it at the start of the game.
- If the user has entered a letter they've already guessed, print the letter and let them know.
- If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
- Import the stages from hangman_art.py and make error go away.

#
