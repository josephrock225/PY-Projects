from random import seed
from random import randint
from os import system, name


class Game:
    def __init__(self) -> None:
        self.num1 = self.rand_number()
        self.num2 = self.rand_number()
        self.ans = self.num1 + self.num2
        self.score = 0

    def rand_number():
        seed()
        return randint(0, 100)


def clear_screen():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')


while True:
    clear_screen()
    game = Game

    #print("Score:", game.score)
    print("What is", game.num1, "+", game.num2, "?")
    in_ans = input()


    if str(in_ans) == "quit":
        exit()
    elif int(in_ans) == game.ans:
        game.score += 1
        break
    else:
        game.score = 0
