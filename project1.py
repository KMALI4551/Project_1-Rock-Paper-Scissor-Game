# Name :- KISHAN KUMAR (CAP-02 BATCH)
# Student_code :- cap02_073

# PROJECT TITLE:- "  ROCK, PAPER, SCISSOR GAME  "

from random import randint

print("\nLet's start the Game 🎮 " + ":- {{{ROCK, PAPER, SCISSOR GAME}}} ")

total_points_gain_by_player = 0
total_points_gain_by_computer = 0

possibilities = ["Rock", "Paper", "Scissor"]
    
dictionary = {"Rock" : "✊", 
              "Paper": "✋", 
              "Scissor": "✂️"}

while True:
  
  print("\nPlayer's turn" + ":- \nRock , Paper , Scissor ?")
  
  Player = input()
    
  while Player != "Rock" and Player != "Paper" and Player != "Scissor":
    print("That's not a Valid Play. Check your Spelling and Correct it")
    Player = input()
    
  print("Player choose -->", dictionary[Player])
  
  computer_move = possibilities[randint(0,2)]
  
  print("\nComputer's turn," + ":- \nRock , Paper , Scissor ?")
  print(computer_move)
  print("computer choose -->",dictionary[computer_move])
  
  print()
  
  
  if Player == computer_move:
      total_points_gain_by_computer += 1
      total_points_gain_by_player += 1
      print("Result is Tie ")
      print("Both selected Same Choice")
      
  elif (Player == "Rock" and computer_move == "Paper"):
      total_points_gain_by_computer += 1
      print("Paper cover the Rock" + "\nComputer Win")
      
  elif (Player == "Scissor" and computer_move == "Rock"):
      total_points_gain_by_computer += 1
      print("Rock break the Scissor" + "\nComputer Win")
      
  elif (Player == "Paper" and computer_move == "Scissor"):
      total_points_gain_by_computer += 1
      print("Scissor cut the Paper easily" + "\nComputer Win")
  
  else:
      total_points_gain_by_player += 1
      print("Player Win")

  print("\nDo you Want to play the game again?")
  user_wish = input()
  
  if user_wish == "no" or user_wish =="No" or user_wish =="Exit" or user_wish =="exit":
    break
  if user_wish != "Yes" and user_wish != "yes":
    print("That's not a Valid Choice. Check your Spelling and Correct it")
    user_wish = input()


print("\nFinal Results are given below :- 👇")
print("Player get " + str(total_points_gain_by_player) + " points")
print("Computer get " + str(total_points_gain_by_computer) + " points")

if total_points_gain_by_player > total_points_gain_by_computer :
  print("\nSo Finally, \nWinner 🏆 --> Player")
elif total_points_gain_by_player < total_points_gain_by_computer :
  print("\nSo Finally, \nWinner 🏆 --> Computer")
else:
  print("\n Points are Same So No one is winner.Game is Draw")