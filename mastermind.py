
from os import system, name
from random import *
from termcolor import colored


class Game:
    def __init__(self):
        self.color_dict = {
            "r": "red",
            "g": "green",
            "b": "blue",
            "p": "magenta",
            "y": "yellow",
            "w": "white"
        }
        self.colors = [i for i in self.color_dict.keys()]
        self.round = 9
        self.guess = []
        self.answer = []
        self.decoding_board = self.init_decoding_board()
        self.key_board = self.init_key_board()

    # decoding_board[round #][col #]
    def init_decoding_board(self) -> list[list]:
        return [["-" for row in range(4)] for col in range(10)]
    
    # key_board[round #][0==black_peg or 1==white_peg]
    def init_key_board(self) -> list[list]:
        return [[" " for row in range(2)] for col in range(10)]

    def won(self) -> bool:
        if self.round != 9:
            return self.key_board[self.round + 1][0] == 4
        return False


def clear_screen():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')


def select_gamemode(game):
    seed()
    while True:
        clear_screen()
        print("Select your gamemode.")
        print("Press 1 for no repeating colors.")
        print("Press 2 to allow repeating colors.")
        print("Type 'quit' to exit.")
        choice = input()

        if choice == "1":
            game.answer = sample(game.colors, 4)
            break  
        elif choice == "2":
            game.answer = choices(game.colors, k=4)           
            break
        elif choice == "quit":
            quit()


def get_input(game):
    def in_colors(guess):
        for i in guess:
            if i not in game.colors:
                return False
        return True

    while True:
        guess = input().lower().replace(' ', '')

        if len(guess) == 4 and in_colors(guess):
            game.decoding_board[game.round] = [i for i in guess]
            break
        else:
            print("Pick 4 colors.")


def check_ans(game):
    black_peg = 0
    white_peg = 0
    ans_copy = game.answer.copy()
    guess_copy = game.decoding_board[game.round].copy()

    # check for correct color correct spot
    for index, ans_letter in enumerate(ans_copy):
        if ans_letter == guess_copy[index]:
            ans_copy[index] = ""
            guess_copy[index] = ""
            black_peg += 1

    # check for correct color incorrect spot
    for i in guess_copy:
        if i != "" and i in ans_copy:
            ans_copy.remove(i)
            white_peg += 1

    game.key_board[game.round][0] = black_peg
    game.key_board[game.round][1] = white_peg


def draw_screen(game):
    # draw the board
    for i in range(10):
        print("|  ", end=" ")
        for j in range(4):
            letter = game.decoding_board[i][j]
            if letter.isalpha():
                print(colored(letter, game.color_dict[letter]), " ", end=" ")
            else:
                print(letter, " ", end=" ")
        print("|   Bl:", game.key_board[i][0], " W:", game.key_board[i][1])
        print()

    # draw the text
    print("Guess 4 colors: ")
    print("Colors:", end =" ")
    for i in range(len(game.colors)):
        print(colored(game.colors[i], game.color_dict[game.colors[i]]), end=" ")
    print()


def main():
    while True:
        game = Game()
        select_gamemode(game)

        while game.round >= -1:
            clear_screen()
            draw_screen(game)

            if game.won():
                print("Winner!")
                break

            if game.round == -1:
                print("Loser!")
                print("The answer was:", *game.answer)
                break
            
            get_input(game)
            check_ans(game)
            game.round -= 1

        input("Press any key.")


main()
