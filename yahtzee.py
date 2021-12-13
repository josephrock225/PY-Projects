import random

def roll_dice():
    random.seed()
    return [random.randint(1, 6) for i in range(5)]


def yahtzee(dice_list):
    return len(set(dice_list)) == 1


def four_oak(dice_list):
    len_check = len(set(dice_list)) == 2
    edge_check = dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]
    return len_check and edge_check


def full_house(dice_list):
    len_check = len(set(dice_list)) == 2
    edge_check = (dice_list[0] == dice_list[1] and dice_list[2] == dice_list[4]) or \
        (dice_list[0] == dice_list[2] and dice_list[3] == dice_list[4])
    return len_check and edge_check


def three_oak(dice_list):
    len_check = len(set(dice_list)) == 3

    for i in range(1, 4):
        if dice_list[i] == dice_list[i - 1] and dice_list[i] == dice_list[i + 1]:
            return len_check

    return False


def small_run(dice_list):
    pairCheck = len(set(dice_list)) == 4 and dice_list[4] - dice_list[0] == 3
    gapCheck = len(set(dice_list)) == 5 and dice_list[3] - dice_list[1] == 2
    return pairCheck or gapCheck


def big_run(dice_list):
    len_check = len(set(dice_list)) == 5
    diff_check = dice_list[4] - dice_list[0] == 4
    return len_check and diff_check


def handCheck(dice_list):
    dice_list.sort()

    if yahtzee(dice_list):
        print("Yahtzee")

    elif four_oak(dice_list):
        print("4 of a kind")
   
    elif full_house(dice_list):
        print("Full House")

    elif three_oak(dice_list):
        print("3 of a kind")

    elif big_run(dice_list):
        print("Big Run")

    elif small_run(dice_list):
        print("Small Run")

    else:
        print("Nothing Special")


def main():
    dice_list = roll_dice()
    print(dice_list)
    print()
    handCheck(dice_list)


main()
