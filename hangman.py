
from os import system, name
from random import seed
from random import randint


def read_words() -> list:
    with open("./words.txt", "r") as f:
        word_list = f.read().splitlines()

    return word_list


def get_random_word() -> str:
    seed()
    random_index = randint(0, len(word_list))
    return word_list[random_index]


def clear_screen():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')


def init_board():
    game_board = ["__" for i in range(len(word_list))]
    return game_board


# Prints the user interface, maybe figure out how to get rid of all the ugly print()
def print_screen(game_board, length, lives, guesses, cheat, gen_word):
    print()
    for i in range(length):
        if "_" in game_board[i]:
            print(game_board[i], " ", end="")
        else:
            print(game_board[i], "  ", end="")

    print()
    print()
    print(lives, "LIVES remaining")
    print("Letters guessed: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    if cheat == True:
        print(gen_word)
    print("Guess letter: ", end="")


# See above
def print_win(lives):
    print()
    print()
    print()
    print("Congrats! You survived with", lives, "lives remaining!")
    print("Press ENTER to start again")
    input()


# See above above
def print_lose(gen_word):
    print()
    print("Game OVER!, the word was", gen_word.upper())
    print("Press ENTER to start again")
    input()


# Validate input
def usr_input():
    while True:
        guess = input()

        if guess == "help":
            print("Here's some helpful commands")
            print("Type 'quit' to end game")
            print("Type 'lives' to gain 6 lives")
            print("Type 'cheat' to reveal answer")
        elif guess == "quit":
            print("Thanks for playing!")
            input()
            exit()
        elif guess == "lives":
            return guess
        elif guess == "cheat":
            return guess
        elif len(guess) != 1 or guess.isalpha() == False:
            print("Not valid input")
        else:
            return guess


# Main
def main():
    while True:
        # inits 
        remaining_guess = 0
        lives = 6
        cheat = False
        gen_word = get_random_word()
        length = len(gen_word)
        game_board = init_board()
        guesses = []

        # Actual game loop
        while True:
            clear_screen()
            print_screen(game_board, length, lives, guesses, cheat, gen_word)

            answer_wrong = True      

            if remaining_guess == length:
                print_win(lives)
                break
            elif lives == 0:
                print_lose(gen_word)
                break

            guess = usr_input()

            if guess == "lives":
                lives += 6
            elif guess == "cheat":
                cheat = True
            else:
                # Check if answer correct and update board
                for i in range(length):
                    if guess == game_board[i]:
                        answer_wrong = False
                        break
                    elif guess == gen_word[i]:
                        game_board.pop(i)
                        game_board.insert(i, guess)
                        remaining_guess += 1
                        answer_wrong = False

                # Wrong answer tracker
                if answer_wrong == True:
                    lives -= 1
                    guesses.append(guess)

word_list = read_words()
main()
