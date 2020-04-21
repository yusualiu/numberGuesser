# This is a program that allows you to guess a correct number
def guessNumber():
  # Introduction
  print('Welcome to Number Guesser game.\nThere are 3 levels; Easy,Medium and Hard.\nPlease enter the level you want to play')   
  levels = ['easy','medium','hard'] #game mode
  boundary = [1,10,20,50] #random generators
  guessess = [6,4,3] #availble guess numbers  
  level = input("Please enter the level here: ")
  # check for easy mode
  if(level.lower() == levels[0]):    
    guessCount = guessess[0]
    minimum = boundary[0]
    maximum = boundary[1]
    displayResult(guessCount,minimum,maximum)
  # check for medium mode
  elif(level.lower() == levels[1]):
    guessCount = guessess[1]
    minimum = boundary[0]
    maximum = boundary[2]
    displayResult(guessCount,minimum,maximum)
  # check for hard mode
  elif(level.lower() == levels[2]):
    guessCount = guessess[2]
    minimum = boundary[0]
    maximum = boundary[3]
    displayResult(guessCount,minimum,maximum)
  # check for wrong mode
  else:
    print('Please try again by entering level mode')




#This displays and process game result     
def displayResult(guessCount,minimum,maximum):
  import random  
  counter = 0
  while(counter < guessCount): 
    setNumber = random.randrange(minimum, maximum)
    guessRemaining = guessCount - counter        
    print(f'You have {guessRemaining} guess more to make')      
    guess = int(input("Please enter your guess: "))      
    if guess == setNumber:
      print("You got it right!")
      break 
    print("That was wrong")
    counter = counter+ 1      
  else:
    print('Game Over')




# starter
guessNumber()