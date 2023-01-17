#!/usr/bin/env python3

#Will we be friends? project
import time
import test


#introduction
print("Welcome to my friend finder!  Maybe we can be friends. Please answer my questions to find out!")
time.sleep(1.5)
print("Ready to begin? Y/N")
intro= input().lower()


if intro in ["y", "yes"]:
  print("Great! Let's get started.")

  #function calls
  test.namequestion()
  test.firstquestion()
  test.secondquestion()
  test.thirdquestion()
  test.fourthquestion()
  test.fifthquestion()
  
  #outro
  time.sleep(2)
  print("Thank you for taking my quiz!")
  
elif intro in ["n", "no"]:
  print("Boooo you're no fun!")
  
else:
  while intro != ["y", "yes", "n", "no"]:
    print("Really...That's not a choice, it's a simple yes or no question... \nReady to begin? Y/N")
    intro= input().lower()
    if intro in ["y", "yes"]:
      print("Great! Let's get started.")
      test.firstquestion()
      test.firstquestion()
      test.secondquestion()
      test.thirdquestion()
      test.fourthquestion()
      test.fifthquestion()

      #outro
      time.sleep(2)
      print("Thank you for taking my quiz!")
      break
      
    elif intro in ["n", "no"]:
      print("Boooo you're no fun!")
      break


print(test.answerweight)