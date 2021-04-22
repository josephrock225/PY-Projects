
from os import system, name
from random import seed
from random import randint


# Count lines in .txt and return random number in range of line count
def rand_word():
    if name == 'nt': 
        f = open("C:\Programming\Python\shit\words.txt", "r", encoding='UTF8')
    else:
        f = open("./words.txt", "r", encoding='UTF8')


    counter = 0
    seed()

    for i in f:
        counter += 1

    f.close()

    return randint(0, counter)


# Assign word to be used from .txt file
def assn_word():
    word_line = rand_word()
    if name == 'nt': 
        f = open("C:\Programming\Python\shit\words.txt", "r", encoding='UTF8')
    else:
        f = open("./words.txt", "r", encoding='UTF8')

    for i in range(word_line):
        gen_word = f.readline().rstrip('\n')

    f.close()
    return gen_word


# Works on linux and windows 0_0
def clear_screen():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')


# Create gameboard, you should figure out that one cool shorthand to make it super cool
def init_board(length):
    game_board = []
    for i in range(length):
        game_board.append("__")
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
        gen_word = assn_word()
        length = len(gen_word)
        game_board = init_board(length)
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


main()
