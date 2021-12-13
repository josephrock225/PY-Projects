import random

def rollDice():
    random.seed()
    return [random.randint(1, 6) for i in range(5)]


def isYahtzee(diceList):
    return len(set(diceList)) == 1


def isFourOAK(diceList):
    lenCheck = len(set(diceList)) == 2
    edgeCheck = diceList[0] == diceList[3] or diceList[1] == diceList[4]
    return lenCheck and edgeCheck


def isFullHouse(diceList):
    lenCheck = len(set(diceList)) == 2
    edgeCheck = (diceList[0] == diceList[1] and diceList[2] == diceList[4]) or \
        (diceList[0] == diceList[2] and diceList[3] == diceList[4])
    return lenCheck and edgeCheck


def isThreeOAK(diceList):
    lenCheck = len(set(diceList)) == 3

    for i in range(1, 4):
        if diceList[i] == diceList[i - 1] and diceList[i] == diceList[i + 1]:
            return lenCheck

    return False


def isSmallRun(diceList):
    pairCheck = len(set(diceList)) == 4 and diceList[4] - diceList[0] == 3
    gapCheck = len(set(diceList)) == 5 and diceList[3] - diceList[1] == 2
    return pairCheck or gapCheck


def isBigRun(diceList):
    lenCheck = len(set(diceList)) == 5
    diffCheck = diceList[4] - diceList[0] == 4
    return lenCheck and diffCheck


def handCheck(dList):
    diceList = dList.copy()
    diceList.sort()

    if isYahtzee(diceList):
        print("Yahtzee")

    elif isFourOAK(diceList):
        print("4 of a kind")
   
    elif isFullHouse(diceList):
        print("full house")

    elif isThreeOAK(diceList):
        print("3 of a kind!")

    elif isBigRun(diceList):
        print("Big Run!!!")

    elif isSmallRun(diceList):
        print("Small Run")


def main():
    dList = rollDice()
    print(dList)
    print()
    handCheck(dList)


def test():
    # Yahtzee
    d = [1,1,1,1,1]
    handCheck(d)

    # 4oak
    d = [1,1,1,1,2]
    handCheck(d)

    # Full house
    d = [1,1,1,2,2]
    handCheck(d)

    # 3oak
    d = [1,1,1,2,3]
    handCheck(d)

    # big run
    d = [1,2,3,4,5]
    handCheck(d)

    # small run
    d = [1,2,3,4,6]
    handCheck(d)


#main()
test()