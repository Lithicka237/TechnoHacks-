import random
def play_game():
  # Prompt users to select rock, paper, or scissors.
  user_choice = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
  # Randomly generate the computer's choice.
  computer_choice = random.choice(['r', 'p', 's'])
  # Determine the winner based on user and computer selections.
  if user_choice == computer_choice:
    print("Tie!")
  elif user_choice == "r" and computer_choice == "s":
    print("You win!")
  elif user_choice == "p" and computer_choice == "r":
    print("You win!")
  elif user_choice == "s" and computer_choice == "p":
    print("You win!")
  else:
    print("You lose!")
  # Display user and computer choices.
  print("You chose:", user_choice)
  print("Computer chose:", computer_choice)
  # Play again?
  play_again = input("Play again? (y/n) ")
  if play_again == "y":
    play_game()
# Start the game
play_game()