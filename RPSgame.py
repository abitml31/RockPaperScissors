'''
Programing language: Python 3.6.0
'''
import random

def RPCgame():
    print("ROCK PAPER SCISSORS GAME\nType \"q\" to quit")
    print("-"*25)
    names = ["paper", "rock", "scissors"]
    while True:
        comp = random.randint(0,2)
        user = input("Type rock, paper or scissors: ").lower()
        if (user == "q"):   return
        userindx = names.index(user)
        print("Computer Chose {}".format(names[comp]))
        if (userindx == comp):
            print("Result: Draw")
        elif (userindx == comp-1):
            print("Result: User Wins")
        else:
            print("Result: Computer Wins")
    
if __name__ == '__main__':
    RPCgame()