# This is a simple quiz game 
# A user will be asked few questions 
# For every right answer user get score 1, 
# and for every wrong answer user get 0. 
# at last total score will be shown 

# This is a simple quiz game 
# A user will be asked few questions 
# For every right answer user get score 1, 
# and for every wrong answer user get 0. 
# at last total score will be shown 

import json
import random
import colorama 
from colorama import Fore, Style, init 

init(autoreset=True)  # initializes colorama

with open('questions.json', 'r') as file: # question.json file holds the questions to be asked in this quiz 
    data = json.load(file)

score = 0
questions = data['quiz']   
question_nos = len(questions)
random.shuffle(questions)

print("\n welcome to the quiz!")

print(f"total number or questions are {question_nos}")
for item in questions:
    user_text = item['question']
    user_answer = item['answer']
    

    user_input = input(Fore.BLUE + f"{user_text} : ")
    if user_input.strip().lower() == user_answer.strip().lower():
        print(Fore.GREEN + "correct answer")
        score +=1
    else:
        print(Fore.RED + f"wronganswer!, correct answer is {user_answer}")


final_score = (score*100)/question_nos
print(Fore.MAGENTA + f"your final score is: {score}/{question_nos}\n and in percentage is: {final_score} % ")
