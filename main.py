#!/usr/bin/env python3

#Will we be friends? project
import time
import logic


#introduction
print("Welcome to my friend finder!  Maybe we can be friends. Please answer my questions to find out!")
time.sleep(1.5)
print("Ready to begin? Y/N")
intro= input().lower()


if intro in ["y", "yes"]:
  print("Great! Let's get started.")

  #function calls
  logic.namequestion()
  logic.firstquestion()
  logic.secondquestion()
  logic.thirdquestion()
  logic.fourthquestion()
  logic.fifthquestion()
  
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
      logic.firstquestion()
      logic.firstquestion()
      logic.secondquestion()
      logic.thirdquestion()
      logic.fourthquestion()
      logic.fifthquestion()

      #outro
      time.sleep(2)
      print("That's it for the quiz!")
      break
      
    elif intro in ["n", "no"]:
      print("Boooo you're no fun!")
      break

# calculations

def weightcalc():
  sumweight= sum(logic.answerweight)
  sumper= (sumweight / 20) * 100
  print(f"Thanks for taking my quiz {logic.username[0]}, we're {sumper}% compatible to be friends.")
  friendslist = open("friendslist.txt", "a")
  friendslist.write(f"{time.asctime(time.localtime(time.time()))} {logic.username[0]} {sumper}% compatible. \n")
  friendslist.close()


weightcalc()
