
def get_input():
    while True:
        num = input("Enter a number: ")

        if num.isdigit():
            return int(num)
        else:
            print("Please enter a number.")


def roman_dict(num):
    roman_dict = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10 : "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M"
    }

    return roman_dict[num]


def num_convert(num):
    roman_string = ""
    while num > 0:
        if num == 1000:
            roman_string += roman_dict(1000)
            num -= 1000
        elif num >= 900:
            roman_string += roman_dict(900)
            num -= 900
        elif num >= 500:
            roman_string += roman_dict(500)
            num -= 500
        elif num >= 400:
            roman_string += roman_dict(400)
            num -= 400
        elif num >= 100:
            roman_string += roman_dict(100)
            num -= 100
        elif num >= 90:
            roman_string += roman_dict(90)
            num -= 90
        elif num >= 50:
            roman_string += roman_dict(50)
            num -= 50
        elif num >= 40:
            roman_string += roman_dict(40)
            num -= 40
        elif num >= 10:
            roman_string += roman_dict(10)
            num -= 10
        elif num >= 9:
            roman_string += roman_dict(9)
            num -= 9   
        elif num >= 5:
            roman_string += roman_dict(5)
            num -= 5
        elif num >= 4:
            roman_string += roman_dict(4)
            num -= 4
        elif num >= 1:
            roman_string += roman_dict(1)
            num -= 1

    return roman_string


print(num_convert(get_input()))