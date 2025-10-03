

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
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("add the item to add: ")
            shopping_list.append(item)
            print(f"item {item} added sucessfully!")
        elif choice == 2:
            item = input("enter the item you want to remove: ")
            shopping_list.remove(item)
            print(f"item {item} removed sucessfully!")
        elif choice == 3:
            print("the lists are: ")
            for item in shopping_list:
                print(item)
        elif choice == 4:
            break
        else:
            print("you're input is incorrect please choose again!")


main()
