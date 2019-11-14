def clean_sentence(sentence):
    sentence = (
        sentence
            .lower()
            .replace(".", "")
            .replace(",", "")
            .replace("'", "")
        )
    return sentence
# sentence = "This is a random sentence with , ' ."
# print(clean_sentence(sentence))

# Got this from the internet: https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
# Iterates through 
def get_key(val, dictionary):
    # Got this from the internet: https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
    # Iterates through each key and value pair in a dictionary. If your given value matches one, it returns the key 
    for key, value in dictionary.items():
        if val == value:
            return key

def count_words():
    user_sentence = input("Give me your favorite sentence. ")
    clean_sentence(user_sentence)
    dictionary = {}
    sentence_words = user_sentence.split(" ")
    for word in sentence_words:
        word_count = user_sentence.count(word)
        dictionary[word] = word_count
    return dictionary

def count_letters():
    user_input = input('Give me a word. ')
    dictionary = {}
    for character in user_input:
        character_count = user_input.count(character)
        dictionary[character] = character_count
    return dictionary

def sort_histogram(dictionary):
    # Need to sort values return from count letters
    # Easy to create a simple list of all the values
    # Could also use list(dictionary.values())
    values = []
    for value in dictionary.values():
        values.append(value)
    # Need to sort the list of values. sorts low to high
    values.sort()
    # Could get errors if sentence isnt at least three words, so checks for that
    if len(values) < 3:
        return print("Your sentence needs to be at least three words.")
    else:
        # gets the key from the three biggest values by working backwards through list
        big_key1 = get_key(values[-1], dictionary)
        big_key2 = get_key(values[-2], dictionary)
        big_key3 = get_key(values[-3], dictionary)
        # the return prints the values here
        return print(f"""The top three words are:
    {dictionary[big_key1]}
    {dictionary[big_key2]}
    {dictionary[big_key3]}""")
    
sort_histogram(count_words())
        