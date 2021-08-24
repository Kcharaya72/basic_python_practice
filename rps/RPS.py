import random


# ROCK PAPER SCISSORS
print("WELCOME TO THE ROCK PAPER SCISSORS GAME\n")
Player1 = input("Enter Your Name : ")
print("player1 is", Player1)
Player2 = "Computer"
print("player2 is", Player2)


# win -- r>s, s>p, p>r
def win():
    if random_choice == choice:
        print("its a tie")
    elif random_choice == 'r' and choice == 's' or random_choice == 's' and choice == 'p' or random_choice == 'p' and choice == 'r':
        print(Player2, ' wins')
    else:
        print(Player1, ' wins')


def full_form(example, p):
    if example == 'r':
        print(f"{p} choice is rock")
    elif example == 'p':
        print(f"{p} choice is paper")
    elif example == 's':
        print(f"{p} choice is scissors")
    else:
        print(" Choice is Invalid")
    return


choice = input("What is your choice r for rock, p for paper, s for scissors ")
full_form(choice, Player1)
random_choice = random.choice(['r', 'p', 's'])
full_form(random_choice, Player2)

win()
