# from bank_account import BankAccount


# def main():
#     deposit_amount = float(
#         input("enter the initial amount you want to deposit: "))

#     amount = BankAccount(deposit_amount)

#     if amount:
#         print(f"deposited: {amount.account_balance}")
#     else:
#         print("wrong input")

#     option = int(
#         input(f"enter the operation you want to perform. \n 1 = withdraw\n 2 = deposit\n 3 = show balance\n"))

#     if option == 1:
#         withdraw = float(input("Enter the amount you want to withdraw: "))
#         amount.withdraw(withdraw)
#         print(f"withdrew: ${withdraw}")
#     elif option == 2:
#         deposit = float(input("enter the amount you want to deposit: "))
#         amount.deposit(deposit)
#         print(f"deposited: ${deposit}")

#     elif option == 3:
#         amount.display_balance()


# main()

# from robust_division_calculator import safe_divide


# def main():
#     numerator = float(input("enter numerator: "))
#     denominator = float(input("enter denominator: "))

#     result = safe_divide(numerator, denominator)

#     print(result)


# main()

from library_management import Book, Library


def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
