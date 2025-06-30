from data import question_data
from question_model import Question
import random
question_bank = []
random_question = random.choice(question_data)

for _ in question_data :
    new_question = Question(random_question["text"] , random_question["answer"])
    question_bank.append(new_question)
    
    print(f"{random_question["text"]} ?"  )
    user_input = input()

    if user_input == "True" :
        new_question.is_true()
