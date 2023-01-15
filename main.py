# While loops + conditionals: Number guessing game!
# Create a program that:
# 1) Generates a random integer between 1 to 10 as the target number
# 2) Asks the user to guess what the random integer is
# 3) If the user guesses incorrectly, say try again and ask them to guess the number again
# 4) If the user guesses correctly, congratulate the user and ask if they want to play again (expect Y or N) 
# 5) If the user presses Y, play again (with a new target number)


# Challenge:
# 6) Create a new random integer to represent the computer's guess at every turn
# 7) Check if the user's guess was closer to the target number or if the computer's guess was closer, and give 1 point to the closer guess
# 8) If either the user or the computer guesses the target number exactly, then award 5 points instead of 1
# 9) Create a scoring system to track number of points the user and computer have
# 10) When the user quits the program, congratulate the winner

from random import randint

# 1-5 only

# target = randint(1,10)
  
# while True:
#   print(target)
#   guess = int(input("Guess the number: (1-10) "))
  
#   if guess < 1 or guess > 10:
#     print("Invalid input, try again!")
#     continue
    
#   if guess == target:
#     again = input("Congratulations! Do you want to play again? (Y/N)")
#   else:
#     print("Try again!")
#     continue
    
#   if again == "N" or again == "n":
#     break
    
#   target =  randint(1,10)
      
      
# 1-10 program

userpoints = 0
computerpoints = 0

while True:
  target = randint(1,10)
  
  print(target)
  
  guess = int(input("Guess the number: (1-10) "))
  
  if guess < 1 or guess > 10:
    print("Invalid input, try again!")
    continue
  
  computer = randint(1,10)
    
  if guess == target or computer == target:
    if guess == target:
      print("You guessed the number! 5 points awarded")
      userpoints += 5
    
    if computer == target:
      print("The computer guesses the number! 5 points awarded")
      computerpoints += 5
  elif abs(guess - target) >= abs(computer - target):
    print("User's guess was closer! 1 point awarded to the user")
    userpoints += 1
  else:
    print("Computer's guess was closer! 1 point awarded to the computer")
    computerpoints += 1
    
  again = input("Do you want to play again? (Y/N)")
    
  if again == "N" or again == "n":
    print("User points: " + str(userpoints))
    print("Computer points: " + str(computerpoints))
    
    if (userpoints > computerpoints):
      print("Congratulations! You won!")
    else:
      print("Oh no! You lost!")
    break