# given a string of letters, return the letter most used in the string

def give_most_letter(string):
    dictionary_of_counts = {}
    most_letter = ""
    count_of_letter = 0
    for letter in string:
        if letter == " ":
            continue
        else:
            dictionary_of_counts[letter] = string.count(letter)
    for key, value in dictionary_of_counts.items():
        if value > count_of_letter:
            count_of_letter = value
            most_letter = key
    return most_letter

print(give_most_letter("hello"))
print(give_most_letter("sprinkles slurps"))
print(give_most_letter("car cat cuts crinkles"))