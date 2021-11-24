
from os import system, name
from random import seed
from random import randint


class Game:
    def __init__(self) -> None:
        self.colors = ["r", "g", "b", "p", "y", "w"]
        self.round = 9
        self.guess = []
        self.answer = self.gen_ans()
        self.decoding_board = self.init_decoding_board()
        self.key_board = self.init_key_board()
        self.black_peg = 0
        self.white_peg = 0

    def gen_ans(self) -> list:
        seed()
        return [self.colors[randint(0,5)] for i in range(0, 4)]

    def init_decoding_board(self) -> list[list]:
        return [["x" for row in range(0, 4)] for col in range(0, 10)]
    
    def init_key_board(self) -> list[list]:
        return [[" " for i in range(0, 2)] for j in range(0, 10)]


def clear_screen():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')


def get_input(game) -> list:
    # check for correct colors
    def in_colors(guess):
        for i in guess:
            if i not in game.colors:
                return False
        return True

    while True:
        guess = input().lower().replace(' ', '')

        # too many letters
        if len(guess) != 4:
            continue

        # letter not in colors list
        if not in_colors(guess):
            continue

        game.guess = [i for i in guess]
        break


def draw_screen(game):
    print()
    for i in range(10):
        print("|  ", end=" ")
        for j in range(4):
            print(game.decoding_board[i][j], " ", end=" ")
        print("|   Bl:", game.key_board[i][0], " W:", game.key_board[i][1])
        print()

    print("Guess 4 colors: ")
    print("Colors:", *game.colors)


def update_board(game):
    #row = abs(game.round - 9)


    for i in range(0,4):
        game.decoding_board[game.round].pop(i)
        game.decoding_board[game.round].insert(i, game.guess[i])

    game.key_board[game.round].pop(0)
    game.key_board[game.round].insert(0, game.black_peg)
    game.key_board[game.round].pop(1)
    game.key_board[game.round].insert(1, game.white_peg)


def check_ans(game):
    game.black_peg = 0
    game.white_peg = 0
    ans_copy = game.answer.copy()
    guess_copy = game.guess.copy()

    # check for correct spot
    for index, ans_letter in enumerate(ans_copy):
        if ans_letter == guess_copy[index]:
            ans_copy.pop(index)
            ans_copy.insert(index, "")
            guess_copy.pop(index)
            guess_copy.insert(index, "")
            game.black_peg += 1

    for i in guess_copy:
        if i != "" and i in ans_copy:
            game.white_peg += 1


def main():
    while True:
        game = Game()

        while game.round >= -1:
            clear_screen()
            draw_screen(game)

            #TODO check for win/loss condition
            if game.black_peg == 4:
                print("Winner!")
                break

            if game.round == -1:
                print("Loser!")
                print("The answer was:", *game.answer)
                break
            
            # get input
            get_input(game)
            
            # check ans
            check_ans(game)

            #TODO update board
            update_board(game)
            
            game.round -= 1

        input()


main()

# game = Game()
# game.answer = ['w', 'g', 'b', 'p']
# game.guess = ['w', 'w', 'w', 'w']
# check_ans(game)
# print("Black:", game.black_peg, "White", game.white_peg)

# game.answer = ['r', 'r', 'r', 'p']
# game.guess = ['p', 'w', 'r', 'r']
# check_ans(game)
# print("Black:", game.black_peg, "White", game.white_peg)