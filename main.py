#!/usr/bin/env python3

#Will we be friends? project
import time
import test

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



#introduction
print("Welcome to my friend finder!  Maybe we can be friends. Please answer my questions to find out!")
time.sleep(1.5)
print("Ready to begin? Y/N")
intro= input().lower()


if intro in ["y", "yes"]:
  print("Great! Let's get started.")
  
  #name question
  def namequestion():
    time.sleep(1.5)
    print("What is your name?")
    name= input()
  
  #function calls
  namequestion()
  test.firstquestion()
  test.secondquestion()
  test.thirdquestion()
  test.fourthquestion()
  test.fifthquestion()
  
  
  #outro
  time.sleep(2)
  print("Thank you for taking my quiz!")
  
elif intro == "n" or intro == "no":
  print("Boooo you're no fun!")
  
else:
  #while intro != "y" or intro != "yes" or intro != "n" or intro != "no":
  while intro != ["y", "yes", "n", "no"]:
    print("Really...That's not a choice, it's a simple yes or no question... \nReady to begin? Y/N")
    intro= input().lower()
    if intro == "y" or intro == "yes":
      print("Great! Let's get started.")
      test.firstquestion()


    #first function of bad answer inside while loop
      def firstquestion():
        time.sleep(1.5)
        print("\n", questions["question1"])
        for x in answers["question1"]:
          print(x)
        user_answer1= input("Enter choice: ").lower()
        if user_answer1 == "b" or user_answer1 == "tippet":
          print("Correct!")
        elif user_answer1 == "a" or user_answer1 == "c" or user_answer1 == "d":
          print("Incorrct, the right answer was B: tippet")
        else:
          print("Incorrct, the right answer was B: tippet")
      
    #second function of bad answer inside while loop   
      def secondquestion():
        time.sleep(1.5)
        print("\n", questions["question2"])
        for x in answers["question2"]:
          print(x)
        user_answer1= input("Enter choice: ").lower()
        if user_answer1 == "a" or user_answer1 == "dry fly":
          print("Correct!")
        elif user_answer1 == "b" or user_answer1 == "c" or user_answer1 == "d":
          print("Incorrct, the right answer was A: dry fly")
        else:
          print("Incorrct, the right answer was A: dry fly")
      
      #third function of bad answer inside while loop
      def thirdquestion():
        time.sleep(1.5)
        print("\n", questions["question3"])
        for x in answers["question3"]:
          print(x)
        user_answer1= input("Enter choice: ").lower()
        if user_answer1 == "d" or user_answer1 == "strike indicator":
          print("Correct!")
        elif user_answer1 == "a" or user_answer1 == "b" or user_answer1 == "c":
          print("Incorrct, the right answer was D: strike indicator") 
        else:
          print("Incorrct, the right answer was D: strike indicator") 
          
      #function calls inside while loop
      firstquestion()
      secondquestion()
      thirdquestion()
      
      #outro inside while loop
      time.sleep(2)
      print("Thank you for taking my quiz!")
      break
      
    elif intro == "n" or intro == "no":
      print("Boooo you're no fun!")
      break