from random import seed
from random import randint
from os import system, name

score = 0

while True:

    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')

    seed()

    number1 = randint(0, 100)
    number2 = randint(0, 100)
    ans = number1 + number2

    while True:
        if name == 'nt': 
            _ = system('cls')

        print("Score:", score)
        print("What is", number1, "+", str(number2) + "?")
        in_ans = input()


        if str(in_ans) == "exit":
            exit()
        elif int(in_ans) == ans:
            score += 1
            break
        else:
            score = 0

    if name == 'nt': 
        _ = system('cls')