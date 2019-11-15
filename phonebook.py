# DICT = {
#         # 'Karen' : '7068598025',
#         # 'Joe' : '7098527065'
# }

# Must have a menu


# What do you want to do (1-5)?
def print_main_menu():
    print("""Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
        """)
    user_selection = int(input("What do you want to do (1-5)? "))
    return user_selection
# 1. Ask them for a person's name, then looks up persons phone number and prints it to the screen
def lookup_entry(dic):
    if len(dic) == 0:
        print()
        print("Phonebook is empty.")
        print()
        return dic
    else:
        try:
            name = input("Name: ")
            print()
            print(f"Phone number: {dic[name]}")
            print()
            return dic
        except KeyError:
            print(f"{name} is not in the phonebook.")
            print()
            return dic
# print(lookup_entry(DICT))

# 2. Prompt them for a name and person's phone number
def set_entry(dictionary):
    print()
    name = input("Name: ")
    number = input("Phone Number: ")
    print()
    dictionary[name] = number
    return dictionary
# set_entry(DICT)
# print(DICT)
# 3. Prompt them for a name and delete entire entry
def delete_entry(dictionary):
    if len(dictionary) == 0:
        print()
        print("Phonebook is empty.")
        print()
        return dictionary
    else:
        try:
            name = input("Name: ")
            print()
            print(f"{name} has been deleted.")
            print()
            del dictionary[name]
            return dictionary
        except KeyError:
            print()
            print(f"{name} is not in the phonebook. ")
            print()
            return dictionary

# delete_entry(DICT)
# print(DICT)
# 4. Go through all entries and print each to the terminal
# realized I want something to print if dictionary is empty
def print_dictionary(dictionary):
    if len(dictionary) == 0:
        print()
        print("There is nothing in your phonebook. ")
        print()
        return dictionary
    else:
        print()
        for key, value in dictionary.items():
            print(f"{key} : {value}")
        print()
        return dictionary
# print_dictionary(DICT)
# 5. Quit the program
def quit_program():
    return False

def main():
    dictionary = {}
    is_running = True
    while is_running:
        try:
            user_selection = print_main_menu()
            if user_selection == 1:
                lookup_entry(dictionary)
            elif user_selection == 2:
                dictionary = set_entry(dictionary)
            elif user_selection == 3:
                dictionary = delete_entry(dictionary)
            elif user_selection == 4:
                print_dictionary(dictionary)
            elif user_selection == 5:
                is_running = quit_program()
                print()
                print("Thank you for using phonebook app. Please rate us on the app store. ")
                print()
            else:
                print()
                print("Please enter a number between 1 and 5.")
                print()
        except ValueError:
            print()
            print("Please enter a number between 1 and 5. ")
            print()

main()