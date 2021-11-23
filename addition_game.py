from random import seed
from random import randint
from os import system, name


class Game:
    def __init__(self) -> None:
        self.num1 = Game.rand_number()
        self.num2 = Game.rand_number()
        self.ans = self.num1 + self.num2

    def rand_number():
        seed()
        return randint(0, 100)


def clear_screen():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')


score = 0

while True:
    clear_screen()
    game = Game()

    print("Score:", score)
    print("What is", game.num1, "+", game.num2, "?")
    in_ans = input()

    if str(in_ans) == "quit":
        exit()
    elif int(in_ans) == game.ans:
        score += 1
    else:
        score = 0
