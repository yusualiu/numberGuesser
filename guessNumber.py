
def guessNumber():
  levels = ['Easy','Medium','Hard']
  guessess = [6,4,3]
  print('Welcome to Number Guesser game.\nThere are 3 levels; Easy,Medium and Hard.\nPlease enter the level you want to play')
  level = input("Please enter the level here: ")

  if(level == levels[0]):
    counter=0
    guessCount = guessess[0]
    while(counter < guessCount): 
      guessRemaining = guessCount - counter     
      import random      
      setNumber = random.randrange(1, 10)
      # print(setNumber)
      print(f'You have {guessRemaining} guess more to make')      
      guess = int(input("Please enter your guess: "))      
      if guess == setNumber:
        print("You got it right!")
        break 
      print("That was wrong")
      counter = counter+ 1      
    else:
      print('Game Over')

    
          




guessNumber()