import random

choices = ['rock', 'paper', 'scissors']

while True:
    playing = input('Do you want to play? (y to play, q to quit): ').lower()
    if playing == 'q':
        print("Thanks for playing! Goodbye!")
        break
    elif playing != 'y':
        print("Invalid choice, please choose 'y' to play or 'q' to quit.")
        continue

    while True:
        player = None
        while player not in choices:
            player = input("Choose rock, paper, or scissors: ").lower()

        computer = random.choice(choices)

        print('Player:', player)
        print('Computer:', computer)

        if player == computer:
            print("It's a draw!")
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'scissors' and computer == 'paper') or \
             (player == 'paper' and computer == 'rock'):
            print("You just won!")
        else:
            print("You just lost!")

        # Ask the player if they want to play again or quit
        play_again = input("Do you want to play again? (y to play again, q to quit): ").lower()
        if play_again == 'q':
            print("Thanks for playing! Goodbye!")
            quit()
            break
