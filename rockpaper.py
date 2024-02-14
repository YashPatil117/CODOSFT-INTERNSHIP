import random

while True:
    player1 = 0
    player2 = 0

    while True:
        input1 = input("Enter an action:\n1. Rock\n2. Paper\n3. Scissor\n4. Exit\n--------------------\n")
        if input1.lower() == "exit" or input1 == "4":
            print("Exiting game.")
            exit()

        input2 = random.choice(['rock', 'paper', 'scissor'])

        print(f"Player 1 chose {input1}, Computer chose {input2}\n")

        if input1 == input2:
            print("That's a tie!\n")
        elif input1 == "rock":
            if input2 == "scissor":
                print("You Win!!!\n")
                player1 += 1
            else:
                print("You Lose :(\n")
                player2 += 1
        elif input1 == "paper":
            if input2 == "rock":
                print("You Win!!!\n")
                player1 += 1
            else:
                print("You Lose :(\n")
                player2 += 1
        elif input1 == "scissor":
            if input2 == "paper":
                print("You Win!!!\n")
                player1 += 1
            else:
                print("You Lose :(\n")
                player2 += 1

        print(f"SCORES!!:\nPlayer 1: {player1}\t Player 2: {player2}\n----------------------------\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    break  
