from bank_account import BankAccount


def main():
    deposit_amount = float(
        input("enter the initial amount you want to deposit: "))

    amount = BankAccount(deposit_amount)

    if amount:
        print(f"you have sucessfully deposited: {amount.account_balance}")
    else:
        print("wrong input")

    option = int(
        input(f"enter the operation you want to perform. \n 1 = withdraw\n 2 = deposit\n 3 = show balance"))

    if option == 1:
        withdraw = float(input("Enter the amount you want to withdraw: "))
        return amount.withdraw(withdraw)
    elif option == 2:
        deposit = float(input("enter the amount you want to deposit: "))

        return amount.deposit(deposit)
    elif option == 3:
        return amount.display_balance


main()
