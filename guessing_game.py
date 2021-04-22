# Tools #####################################
def word_sep(word):
    letters = []
    for letter in word:
        letters.append(letter)
    return letters


def acc_dict(in_letter, check_letter):
    acc_dict = {
        "q": "`12wsa",
        "w": "123qeasd",
        "e": "234wrsdf",
        "r": "345etdfg",
        "t": "456ryfgh",
        "y": "567tughj",
        "u": "678yihjk",
        "i": "789uojkl",
        "o": "890ipkl",
        "p": "90-o[l;'",
        "a": "qwszx",
        "s": "qweadzxc",
        "d": "wersfxcv",
        "f": "ertdgcvb",
        "g": "rtyfhvbn",
        "h": "tyugjbnm",
        "j": "yuihknm,",
        "k": "uiojlm,.",
        "l": "iopk;,./",
        "z": "asx",
        "x": "asdzc",
        "c": "sdfxv",
        "v": "dfgcb",
        "b": "fghvn",
        "n": "ghjbm",
        "m": "hjkn,"
    }
    
    if in_letter.lower() == check_letter.lower():
        return 1.0

    for key in acc_dict:
        if in_letter.lower() in acc_dict[key] and check_letter.lower() == key:
            return 0.5

    return 0.0


def input_accuracy(check_word, in_word):
    check_list = word_sep(check_word)
    in_list = word_sep(in_word)

    i = 0
    accy = 0

    #If input is longer
    if len(check_list) > len(in_list):
        length = len(in_list)
    #If input is short
    else:
        length = len(check_list)

    while i < length:
        try:
            if acc_dict(in_list[i], check_list[i]) == 0:
                in_list.pop(i)
            else:   
                accy += acc_dict(in_list[i], check_list[i])
                i += 1

        except IndexError:
            return 0

    return accy / len(check_list)
    

#Game stuff#####################################
def y_or_n():
    while True:
        ans = input()
        if input_accuracy("yes", ans) >= .5:
            return True
        elif input_accuracy("no", ans) >= .5:
            return False
        else:
            print("Hint, type yes or no")


def h_or_l():
    while True:
        ans = input()
        if input_accuracy("higher", ans) >= .5:
            return True
        elif input_accuracy("lower", ans) >= .5:
            return False
        print("Hint, type higher or lower")



def is_correct():
    num = 50
    acc = 25

    while True:
        print("Is it", str(num) + "?")
        if y_or_n():
            print("I got it right, loser.")
            return
        else:
            print("Is the number higher or lower?")
            if h_or_l():
                num = num + acc
            else:
                num = num - acc
            acc = round(acc / 2)



def main():
    print("Think of a number between 1-99")
    is_correct()


main()
