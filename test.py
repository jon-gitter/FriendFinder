import time

questions= {
  "question1": "What is your ideal vacation destination?",
  "question2": "What is your favorite movie genre?",
  "question3": "What do you like to do for fun?",
  "question4": "What is your favorite type of adult beverage?",
  "question5": "What is your favorite casual conversation topic?",
}

answers= {
  "answer1": ["A: beach resort", "B: camping in the mountains", "C: clubbing downtown", "D: exploring historical sites"],
  "answer2": ["A: action", "B: scifi/fantasy", "C: romcom", "D: drama"],
  "answer3": ["A: outdoors stuff", "B: gaming", "C: dancing", "D: workout"],
  "answer4": ["A: wine", "B: beer", "C: hard seltzer", "D: mixed drink"],
  "answer5": ["A: what do you for work?", "B: weather", "C: sports", "D: current location/venue"]
}

answerweight= []


def firstquestion():
    time.sleep(1.5)
    print("\n", questions["question1"])
    for x in answers["answer1"]:
      print(x)
    user_answer1= input("Enter choice: ").lower()
    if user_answer1 == "a":
      print(f"You chose --> {answers['answer1'][0]}")
      answerweight.append(4)
    elif user_answer1 == "b":
      print(f"You chose --> {answers['answer1'][1]}")
      answerweight.append(2)
    elif user_answer1 == "c":
      print(f"You chose --> {answers['answer1'][2]}")
      answerweight.append(1)
    elif user_answer1 == "d":
      print(f"You chose --> {answers['answer1'][3]}")
      answerweight.append(3)

#second function   
def secondquestion():
  time.sleep(1.5)
  print("\n", questions["question2"])
  for x in answers["answer2"]:
    print(x)
  user_answer1= input("Enter choice: ").lower()
  if user_answer1 == "a":
    print(f"You chose --> {answers['answer2'][0]}")
    answerweight.append(3)
  elif user_answer1 == "b":
    print(f"You chose --> {answers['answer2'][1]}")
    answerweight.append(2)
  elif user_answer1 == "c":
    print(f"You chose --> {answers['answer2'][2]}")
    answerweight.append(1)
  elif user_answer1 == "d":
    print(f"You chose --> {answers['answer2'][3]}")
    answerweight.append(4)
  elif user_answer1 != ["a", "b", "c", "d"]:
    print("Please choose A, B, C, or D to continue")
      

#third function
def thirdquestion():
  time.sleep(1.5)
  print("\n", questions["question3"])
  for x in answers["answer3"]:
    print(x)
  user_answer1= input("Enter choice: ").lower()
  if user_answer1 == "a":
    print(f"You chose --> {answers['answer3'][0]}")
    answerweight.append(4)
  elif user_answer1 == "b":
    print(f"You chose --> {answers['answer3'][1]}")
    answerweight.append(3)
  elif user_answer1 == "c":
    print(f"You chose --> {answers['answer3'][2]}")
    answerweight.append(1)
  elif user_answer1 == "d":
    print(f"You chose --> {answers['answer3'][3]}")
    answerweight.append(2)
  elif user_answer1 != ["a", "b", "c", "d"]:
    print("Please choose A, B, C, or D to continue")


#fourth function
def fourthquestion():
  time.sleep(1.5)
  print("\n", questions["question4"])
  for x in answers["answer4"]:
    print(x)
  user_answer1= input("Enter choice: ").lower()
  if user_answer1 == "a":
    print(f"You chose --> {answers['answer4'][0]}")
    answerweight.append(2)
  elif user_answer1 == "b":
    print(f"You chose --> {answers['answer4'][1]}")
    answerweight.append(4)
  elif user_answer1 == "c":
    print(f"You chose --> {answers['answer4'][2]}")
    answerweight.append(1)
  elif user_answer1 == "d":
    print(f"You chose --> {answers['answer4'][3]}")
    answerweight.append(3)
  elif user_answer1 != ["a", "b", "c", "d"]:
    print("Please choose A, B, C, or D to continue")

#fifth function
def fifthquestion():
  time.sleep(1.5)
  print("\n", questions["question5"])
  for x in answers["answer5"]:
    print(x)
  user_answer1= input("Enter choice: ").lower()
  if user_answer1 == "a":
    print(f"You chose --> {answers['answer5'][0]}")
    answerweight.append(3)
  elif user_answer1 == "b":
    print(f"You chose --> {answers['answer5'][1]}")
    answerweight.append(1)
  elif user_answer1 == "c":
    print(f"You chose --> {answers['answer5'][2]}")
    answerweight.append(2)
  elif user_answer1 == "d":
    print(f"You chose --> {answers['answer5'][3]}")
    answerweight.append(4)
  elif user_answer1 != ["a", "b", "c", "d"]:
    print("Please choose A, B, C, or D to continue")
