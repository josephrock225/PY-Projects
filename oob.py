input_file = open("constitution.txt", "r")
output_file = open("translation.txt", "a")


def is_vowel(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Oob"
            else:
                translation = translation + "oob"
        else:
            translation = translation + letter
    return translation


output_file.write(is_vowel(input_file.read()))


input_file.close()
output_file.close()
