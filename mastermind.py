
from os import system, name
from random import seed
from random import randint


class Game:
    def __init__(self) -> None:
        self.colors = ["r", "g", "b", "p", "y", "w"]
        self.code_pattern = self.gen_ans()
        self.decoding_board = self.init_decoding_board()
        self.key_board = self.init_key_board()

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


def draw_screen(game_board, wObl_board):
    game = Game()
    print()
    for i in range(10):
        print("|  ", end=" ")
        for j in range(4):
            print(game_board[i][j], " ", end=" ")
        print("|   Bl:", wObl_board[i][0], " W:", wObl_board[i][1])
        print()

    print("Guess 4 colors seperated by spaces: ")
    print("Colors:", *game.colors)


def update_board(game_board, guess_list, wObl_board, wObl_list, counter):
    for i in range(0,4):
        game_board[counter].pop(i)
        game_board[counter].insert(i, guess_list[i])
    for i in range(0,2):
        wObl_board[counter].pop(i)
        wObl_board[counter].insert(i, wObl_list[i])

    return game_board, wObl_board


# done
def gen_ans():
    colors = [
        "r",
        "g",
        "b",
        "p",
        "y",
        "w"
    ]
    seed()
    answer = [colors[randint(0,5)] for i in range(0, 4)]

    return answer


# done
def init_board():
    return [["x" for i in range(0, 4)] for j in range(0, 10)], [[" " for i in range(0, 2)] for j in range(0, 10)]


def input_par():
    while True:
        counter = 0
        li_item = ""
        guess_list = []
        fail = False

        guess = input()

        for i in guess:
            if i == " ":
                guess_list.insert(counter, li_item)
                li_item = ""
                counter += 1
            else:
                li_item += i

        guess_list.insert(counter, li_item)

        # Failed input situations
        for i in range(len(guess_list)):
            if len(guess_list[i]) != 1 or guess_list[i] not in "rgbpyw":
                fail = True
                break

        if len(guess_list) == 4 and fail == False:
            return guess_list
        else:
            print("Guess 4 colors (listed above) seperated by spaces: ")


def check_ans(guess_list, ans_list):
    guess = []
    ans = []
    bl = 0
    w = 0

    for i in range(4):
        guess.append(guess_list[i])
        ans.append(ans_list[i])

    i = 3
    while i >= 0:
        if guess[i] == ans_list[i]:
            guess.pop(i)
            ans.pop(i)
            bl += 1
        i -= 1

    max = len(guess)

    for i in range(max):
        for j in range(max):
            if guess[i] == ans[j]:
                w += 1
                ans.pop(j)
                ans.insert(j, "")

    return [bl, w]


def main():
    while True:
        ans_list = gen_ans()
        game_board, wObl_board = init_board()
        wObl_list = [" ", " "]
        counter = 9

        while True:
            clear_screen()
            draw_screen(game_board, wObl_board)

            if wObl_list[0] == 4:
                print("Winner!")
                input()
                break
            elif counter < 0:
                print("end of game")
                input()
                break
            
            guess_list = input_par()
            wObl_list = check_ans(guess_list, ans_list)
            game_board, wObl_board = update_board(game_board, guess_list, wObl_board, wObl_list, counter)
            counter -= 1


main()