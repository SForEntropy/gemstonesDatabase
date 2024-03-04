import readStones
import addStone
import updateStones
import deleteStones
import searchStones

def read_file(file_path):
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")

def gemstones_menu():
    option = 0
    options_list = ["1", "2", "3", "4", "5", "6"]
    menu_choices = read_file("Python\Gemstones\stonesMenuOptions.txt")  

    while option not in options_list:
        print(menu_choices)
        option = input("Enter an option from the menu choices above: ")

        if option not in options_list:
            print(f"The {option} variable is not a valid choice.")

    return option

main_program = True
while main_program:
    main_menu = gemstones_menu()

    match main_menu:
        case "1":
            readStones.read_gemstones()
        case "2":
            addStone.insert_gemstone()
        case "3":
            updateStones.update_gemstone()
        case "4":
            deleteStones.delete_gemstone()
        case "5":
            searchStones.search_gemstone()
        case _:
            main_program = False

input("Press enter to exit...")