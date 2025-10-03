

def display_menu():
    print("Shopping List Manager")
    # add = int(input("1. Add Item"))
    # remove = int(input("2. Add Item"))
    # view = int(input("3. Add Item"))
    # exit = int(input("4. Add Item"))
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    while True:
        display_menu()
        shopping_list = []
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("add the item of your choice")
            shopping_list.append(item)
        elif choice == 2:
            item = input("enter the item you want to remove")
            shopping_list.remove(item)
        elif choice == 3:
            print("the list is ", shopping_list)
        elif choice == 4:
            break
        else:
            print("you're input is incorrect please choose again")


main()
