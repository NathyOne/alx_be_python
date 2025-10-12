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

from robust_division_calculator import safe_divide


def main():
    numerator = float(input("enter numerator: "))
    denominator = float(input("enter denominator: "))

    result = safe_divide(numerator, denominator)

    print(result)


main()
