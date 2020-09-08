# 1 for Checking Account
# 2 for Savings Account


def extract_money(account_type, amount):
    print("Amount to extract "+str(amount) +
          " account_type is "+str(account_type))
    if(amount % 500 == 0 and amount > 0 and 0 < account_type < 3):  # conditions to be checked
        flag = 1
        if(account_type == 1):
            f = open(
                "checking_account_balance.txt", "r")
            chk_bal = int(f.read())
            if(chk_bal > amount):
                chk_bal -= amount
            else:
                flag = 0
            f.close()
            if(flag == 1):
                f = open(
                    "checking_account_balance.txt", "w")
                f.write(str(chk_bal))
                f.close()
                f = open(
                    "checking_account_transaction.txt", "a")
                f.write(str("Debit "+str(amount))+"\n")
                f.close()
        elif(account_type == 2):
            f = open(
                "savings_account_balance.txt", "r")
            sav_bal = int(f.read())
            if(sav_bal > amount):
                sav_bal -= amount
            else:
                flag = 0
            f.close()
            if(flag == 1):
                f = open(
                    "savings_account_balance.txt", "w")
                f.write(str(sav_bal))
                f.close()
                f = open(
                    "saving_account_transaction.txt", "a")
                f.write("Debit "+str(amount)+"\n")
                f.close()
        if(flag == 1):
            print("Transaction successfull")
        else:
            print("Not Sufficient Amount to extract")
    else:
        print("Not valid amount or account type to extract")


def add_money(account_type, amount):
    print("Amount to add "+str(amount) +
          " account_type is "+str(account_type))
    if(amount % 500 == 0 and amount > 0 and 0 < account_type < 3):  # conditions to be checked
        if(account_type == 1):
            f = open(
                "checking_account_balance.txt", "r")
            chk_bal = int(f.read())
            chk_bal += amount
            f.close()
            f = open(
                "checking_account_balance.txt", "w")
            f.write(str(chk_bal))
            f.close()
            f = open(
                "checking_account_transaction.txt", "a")
            f.write("Credit "+str(amount)+"\n")
            f.close()
        if(account_type == 2):
            f = open(
                "savings_account_balance.txt", "r")
            chk_bal = int(f.read())
            chk_bal += amount
            f.close()
            f = open(
                "savings_account_balance.txt", "w")
            f.write(str(chk_bal))
            f.close()
            f = open(
                "saving_account_transaction.txt", "a")
            f.write("Credit "+str(amount)+"\n")
            f.close()
        print("Transaction successfull")
    else:
        print("Not valid amount or account type to extract")


if __name__ == '__main__':

    extract_money(2, -10)
    print()
    extract_money(2, 20)
    print()
    extract_money(2, 3000)
    print()
    add_money(2, 40)
    print()
    add_money(2, 4000)
    print()

    extract_money(2, 12000)
    print()

    extract_money(1, 0)
    print()
    extract_money(1, 20)
    print()
    extract_money(1, 2000)
    print()
    add_money(1, 40)
    print()
    add_money(1, 1000)
    print()

    print("Saving account Transactions")
    f = open(
        "saving_account_transaction.txt", "r")
    saving_transactions = f.read()
    print(saving_transactions)
    f.close()

    print()
    print("Saving account Final Balance")
    f = open(
        "savings_account_balance.txt", "r")
    print(f.read())
    f.close()

    print()
    print("Checking account Transactions")
    f = open(
        "checking_account_transaction.txt", "r")
    checking_transactions = f.read()
    print(checking_transactions)
    f.close()

    print()
    print("Checking account Final Balance")
    f = open(
        "checking_account_balance.txt", "r")
    print(f.read())
    f.close()
