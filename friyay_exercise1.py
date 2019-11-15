# [1,2,3,4], [1,2,3,4] = true
# [1,2,3,4], [1,4,5,6] = false
# [1,2,3,4],[1,4,4,2] = false
# [1,2,3,4],[1,4,3,2] = true
# [1,2,3,4,5],[1,2,3,4] = false;



def check_arrays(array1, array2):
    dictionary = {}
    dictionary2 = {}
    for number in array1:
        dictionary[number] = array1.count(number)
    # print(dictionary)
    for number in array2:
        dictionary2[number] = array2.count(number)
    # print(dictionary2)
    if len(dictionary) != len(dictionary2):
        return False
    try:
        for key in dictionary.keys():
            if dictionary[key] != dictionary2[key]:
                return False
        return True
    except KeyError:
        return False

# print(check_arrays([1,2,3,4], [1,2,3,4, 5]))
print(check_arrays([1,2,3,4], [1,2,3,4]))
print(check_arrays([1,2,3,4], [1,4,5,6]))
print(check_arrays([1,2,3,4],[1,4,4,2]))
print(check_arrays([1,2,3,4],[1,4,3,2]))
print(check_arrays([1,2,3,4,5],[1,2,3,4]))
# You count the number of each number
# Then compare the len of the dictionaries to make sure they have the same number of numbers