# 1. Display a menu asking whether to check in or out
# 2. Prompt the user for a floor number, then a room number
# 3. If checking in, ask for the number of occupants and what their names are.
# 4. If checking out, remove the occupants from that room
# 5. Do not allow anyone to check into a room that is already occupied.
# 6. Do not allow checking out of a room that isn't occupied
# Menu mockup:
# Hotel Manager.io
# ================
# 1. Check in
# 2. Check out
# 3. Current occupants
# 4. Quit

# 1. Check in
def print_main_menu():
    no_mistakes = True
    while no_mistakes:
        print("""Hotel Manager.io
================
1. Check in
2. Check out
3. Current occupants
4. Quit
""")
        try:
            choice = int(input("What do you want to do? "))
            if choice in range(1, 5):
                no_mistakes = False
            else:
                print("Please enter a number between 1 and 4")
        except ValueError:
            print("Please enter a number between 1 and 4")
    return choice

def check_in(dictionary):
    floor_number = input("Floor number: ")
    if floor_number not in dictionary:
        dictionary[floor_number] = {}
    room_number = input("Room number: ")
    if room_number in dictionary[floor_number]:
        print("Room is occupied")
        return dictionary
    try:
        number_of_occupants = int(input("Number of occupants: "))
    except ValueError:
        print("Please enter a number. ")
        return dictionary
    dictionary[floor_number][room_number] = []
    names_added = 0
    while names_added < number_of_occupants:
        occupant_name = input("Occupant name: ")
        dictionary[floor_number][room_number] += [occupant_name]
        names_added += 1
    return dictionary

def check_typo(name):
    print(f"Entry does not match {name} records.")
    check = input("Do you want to go back to the main menu? Type yes to return to main menu. ")
    if check == "yes":
        return False
    else:
        return True
    

    # I need to figure out how to create dictionaries within dictionaries
    # If you just add stuff on the left hand side of a dictionary item creation, it will create dictionaries in dictionaries for you


# 2. Check out
def check_out(dictionary):
    while True:
        floor_number = input("Floor number: ")
        if dictionary.get(floor_number) == None:
            if check_typo("floor"):
                continue
            else:
                return dictionary
        room_number = input("Room number: ")
        if dictionary[floor_number].get(room_number) == None:
            if check_typo("room"):
                continue
            else:
                return dictionary
        check = input(f"Are you sure you want to check out {room_number}? Type yes to continue. ")
        if check == "yes":
            del dictionary[floor_number][room_number]
            return dictionary
    return dictionary

def print_current_occupants(dictionary):
    print("The current occupants of the hotel are: ")
    for floor in dictionary.keys():
        for room in dictionary[floor].keys():
            for occupant in dictionary[floor][room]:
                print(f"{occupant} is staying in room {room} on floor {floor}")
    return dictionary

def quit():
    return False

def clean_up_floors(dictionary):
    variable = []
    for floor in dictionary:
        if dictionary[floor] == {}:
            variable.append(floor)
    for x in variable:
        del dictionary[x]
    return dictionary
    

def main():
    is_running = True
    dictionary = {}
    while is_running:
        dictionary = clean_up_floors(dictionary)
        choice = print_main_menu()
        if choice == 1:
            check_in(dictionary)
        elif choice == 2:
            check_out(dictionary)
        elif choice == 3:
            print_current_occupants(dictionary)
        elif choice == 4:
            is_running = quit()
        print(dictionary)
    print("Thank you for using Hotel Manager.io")
main()