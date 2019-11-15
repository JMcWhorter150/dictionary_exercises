# [1,2,3,4], [1,4,9,16] = true
# [1,2,3,4], [1,4,5,6] = false
# [1,2,3,4],[1,4,4,2] = false
# [1,2,3,4],[1,16,9,4] = true
# [1,2,3,4,5],[1,2,3,4] = false

# make a dictionary
# make a function true or false
# function should return if each value in first array contains second power in second array
def checks_second_power_array(array1, array2):
    dictionary = {}
    for number in array1:
        dictionary[number] = number * number
    for key in dictionary.keys():
        if dictionary[key] not in array2:
            return False
    return True

print(checks_second_power_array([1,2,3,4], [1,4,9,16]))
print(checks_second_power_array([1,2,3,4], [1,4,5,6]))
print(checks_second_power_array([1,2,3,4],[1,4,4,2]))
print(checks_second_power_array([1,2,3,4],[1,16,9,4]))
print(checks_second_power_array([1,2,3,4,5],[1,2,3,4]))