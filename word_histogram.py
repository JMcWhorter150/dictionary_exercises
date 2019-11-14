# ask user for sentence to be input
user_sentence = input("Give me your favorite sentence. ")
user_sentence = user_sentence.lower()
user_sentence = user_sentence.replace(".", "")
user_sentence = user_sentence.replace(",", "")
user_sentence = user_sentence.replace("'", "")
# make a dictionary
dictionary = {}
# split sentence into individual words
sentence_words = user_sentence.split(" ")
# work through each word in list and count it
# then add the word and count to dictionary
for word in sentence_words:
    word_count = user_sentence.count(word)
    dictionary[word] = word_count

print(dictionary)
# realized capitals will mess this up, made everything lower
# realized punctuation messes things up, removed commas and periods