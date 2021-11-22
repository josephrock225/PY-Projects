
from os import system, name
from random import seed
from random import randint


class Game:
    def __init__(self, word) -> None:
        self.word = word
        self.word_length = len(self.word)
        self.guesses = []
        self.lives = 6
        self.is_cheating = False
        self.game_board = ["__" for i in range(self.word_length)]

    def guess(self, letter):
        # if correct
        if letter in self.word:
            for index, l in enumerate(self.word):
                if l == letter:
                    self.game_board.pop(index)
                    self.game_board.insert(index, letter)

        # if incorrect
        else:
            self.guesses.append(letter.lower())
            self.lives -= 1

    def cheat(self):
        self.is_cheating = True

    def add_lives(self, num):
        self.lives += num


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
    game_board = ["__" for i in range(word_length)]
    return game_board


def print_screen(game):
    print()
    print(*game.game_board, ' ')
    print()
    print()
    print(game.lives, "LIVES remaining")
    print("Letters guessed: ", *game.guesses)
    print()
    if game.is_cheating:
        print(game.word)
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
        game = Game(get_random_word())

        # Actual game loop
        while True:
            clear_screen()
            print_screen(game)

            answer_wrong = True      

            if "__" not in game.game_board:
                print_win(game.lives)
                break
            elif game.lives == 0:
                print_lose(game.word)
                break

            guess = usr_input()

            if guess == "lives":
                game.add_lives(6)
            elif guess == "cheat":
                game.cheat()
            elif guess == "quit":
                quit_game()
            elif guess == "help":
                print_help()
            else:
                # Check if answer correct and update board
                game.guess(guess)

word_list = read_words()
main()

game = Game(get_random_word())
print(game.guesses)
print(game.word)
print(game.word_length)
game.guess("A")
print(game.guesses)
