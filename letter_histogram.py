# Take user input of a string
user_input = input('Give me a word. ')
# Make a dictionary
dictionary = {}
# dictionary contains how many times each letter was used in word
# work through each character in input, count how many times it exists in string,
# then counts how many each appears, then adds them to dictionary
for character in user_input:
    character_count = user_input.count(character)
    dictionary[character] = character_count
# Thought I was going to have to add an if statement for multiple characters
# but, each time you have character, will just update the value to the same thing
print(dictionary)