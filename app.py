# This is a simple quiz game 
# A user will be asked few questions 
# For every right answer user get score 1, 
# and for every wrong answer user get 0. 
# at last total score will be shown 

print("welcome users")

question1 = "what is the capital of India: "
answer1 = "Delhi"
question2 = "which element has atomic number 1: "
answer2 = "Hydrogen"
question3 = "what is capital of haryana: "
answer3 = "chandigarh"



marks =[]

# this is for question 1 

input1 = input(question1)
if input1.lower() == answer1.lower():
    marks.append(1)
    print("correct answer")
else:
    print(f"wrong answer, correct answer was {answer1}")

# this is for 2nd question
input2 = input(question2)
if input2.lower() == answer2.lower():
    marks.append(1)
    print("correct answer")
else:
    print(f"wrong answer, correct answer was {answer2}")

# this is for 3rd question
input3 = input(question3)
if input3.lower() == answer3.lower():
    marks.append(1)
    print("correct answer")
else:
    print(f"wrong answer, correct answer was {answer3}")


total_marks = len(marks)  
print(f"your total marks: {total_marks}")
    