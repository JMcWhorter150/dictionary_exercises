# Make a function
# accepts two strings
# returns true if anagrams
# returns false if not anagrams

# "pie", "eip" = true
# "pie", "pie" = true
# "pie", "pies" = false
# "pie", "pwe" = false

def check_anagrams(str1, str2):
    dictionary = {}
    dictionary2 = {}
    for number in str1:
        dictionary[number] = str1.count(number)
    print(dictionary)
    for number in str2:
        dictionary2[number] = str2.count(number)
    print(dictionary2)
    if len(dictionary) != len(dictionary2):
        return False
    try:
        for key in dictionary.keys():
            if dictionary[key] != dictionary2[key]:
                return False
        return True
    except KeyError:
        return False

print(check_anagrams("pie", "eip"))
print(check_anagrams("pie", "pie"))
print(check_anagrams("pie", "pies"))
print(check_anagrams("pie", "pwe"))




















