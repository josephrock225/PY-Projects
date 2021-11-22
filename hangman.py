
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

    # TODO fix logic
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


def get_random_word() -> str:
    with open("./words.txt", "r") as f:
        word_list = f.read().splitlines()

    seed()
    random_index = randint(0, len(word_list))
    return word_list[random_index]


def clear_screen():
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')


def print_screen(game):
    print(*game.game_board, ' ')
    print()
    print()
    print(game.lives, "LIVES remaining")
    print("Letters guessed: ", *game.guesses)
    print()
    if game.is_cheating:
        print(game.word)
    print("Guess letter: ", end="")


def print_win(lives):
    print("Congrats! You survived with", lives, "lives remaining!")
    print("Press ENTER to start again")
    print()
    input()


def print_lose(guess_word):
    print("Game OVER!, the word was", guess_word.upper())
    print("Press ENTER to start again")
    print()
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


def usr_input(game):
    while True:
        guess = input()

        if guess == "lives":
            game.add_lives(6)
            break
        elif guess == "cheat":
            game.cheat()
            break
        elif guess == "quit":
            quit_game()
        elif guess == "help":
            print_help()
        elif len(guess) != 1 or guess.isalpha() == False:
            print("Not valid input")
        else:
            game.guess(guess)
            break


def main():
    while True:
        game = Game(get_random_word())

        while True:
            clear_screen()
            print_screen(game)    

            if "__" not in game.game_board:
                print_win(game.lives)
                break
            elif game.lives == 0:
                print_lose(game.word)
                break

            usr_input(game)

main()
