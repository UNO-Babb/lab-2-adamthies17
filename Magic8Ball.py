#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["As I see it, yes", "Ask again later", "Better not tell you now", "You might be onto something", "Absolutely", "Definitely not", "It may be possible...", "I don't think so...", "Yes", "No"]
  #Answer question randomly with one of the options from your earlier list.

  num = random.random() 
  num = num * 1000
  num = int(num)
  things = len(answers)
  num = num % things

  question = input("Ask me a question: ")
  print(answers[num])
if __name__ == '__main__':
  main()
