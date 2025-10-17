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

with open('questions.json', 'r') as file: # question.json file holds the questions to be asked in this quiz 
    data = json.load(file)

score = 0
questions = data['quiz']   
question_no = len(questions)

print("\n welcome to the quiz!")

print(f"total number or questions are {question_no}")
for item in questions:
    user_text = item['question']
    user_answer = item['answer']
    

    user_input = input(f"{user_text} : ")
    if user_input.strip().lower() == user_answer.strip().lower():
        print("correct answer")
        score +=1
    else:
        print(f"wronganswer!, correct answer is {user_answer}")

print(f"your final score is: {score}")