
from os import system, name
from random import seed
from random import randint


class GameBoard:
    def __init__(self, word) -> None:
        self.word = word
        self.word_length = len(word)
        self.guesses = []

    def guess(self, letter):
        self.guesses.append(letter.lower())


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


def init_board(word_length):
    game_board = ["__ " for i in range(word_length)]
    return game_board


def print_screen(game_board, lives, guesses, cheat, guess_word):
    print()
    print(*game_board, ' ')
    print()
    print()
    print(lives, "LIVES remaining")
    print("Letters guessed: ", *guesses, ' ')
    print()
    if cheat == True:
        print(guess_word)
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
def print_lose(guess_word):
    print()
    print("Game OVER!, the word was", guess_word.upper())
    print("Press ENTER to start again")
    input()


def print_help():
    print("Here's some helpful commands")
    print("Type 'quit' to end game")
    print("Type 'lives' to gain 6 lives")
    print("Type 'cheat' to reveal answer")
    print()


def quit_game():
    print("Thanks for playing!")
    input()
    exit()


# TODO fix logic
def usr_input():
    while True:
        keywords = ["help", "quit", "lives", "cheat"]
        guess = input()

        if guess in keywords:
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
        guess_word = get_random_word()
        word_length = len(guess_word)
        game_board = init_board(word_length)
        guesses = []

        # Actual game loop
        while True:
            clear_screen()
            print_screen(game_board, lives, guesses, cheat, guess_word)

            answer_wrong = True      

            if remaining_guess == word_length:
                print_win(lives)
                break
            elif lives == 0:
                print_lose(guess_word)
                break

            guess = usr_input()

            if guess == "lives":
                lives += 6
            elif guess == "cheat":
                cheat = True
            elif guess == "quit":
                quit_game()
            elif guess == "help":
                print_help()
            else:
                # Check if answer correct and update board
                for i in range(word_length):
                    if guess == game_board[i]:
                        answer_wrong = False
                        break
                    elif guess == guess_word[i]:
                        game_board.pop(i)
                        game_board.insert(i, guess)
                        remaining_guess += 1
                        answer_wrong = False

                # Wrong answer tracker
                if answer_wrong == True:
                    lives -= 1
                    guesses.append(guess)

word_list = read_words()
#main()

game = GameBoard(get_random_word())
print(game.guesses)
print(game.word)
print(game.word_length)
game.guess("A")
print(game.guesses)
