number = input("Input a number: ")
#number_len = len(number)

ones = ["one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "Zero "]

if len(number) == 1 and number[0] == "0":
    print(ones[9])

print(ones[-1])