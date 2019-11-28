principal = int(input("Enter the credit principal:\n"))
command = input("What do you want to calculate?\ntype 'm' - for count of months,\ntype 'p' - for monthly payment:")
if command == "m":
    payment = int(input("Enter monthly payment:\n"))
    period = principal // payment
    if period == 1:
        print("\nIt takes 1 month to repay the credit")
    else:
        if principal % payment == 0:
            print("\nIt takes {0} months to repay the credit".format(period))
        else:
            print("\nIt takes {0} months to repay the credit".format(principal // payment + 1))
elif command == "p":
    count = int(input("Enter count of months:\n"))
    payment = principal // count
    if payment * count == principal:
        print("\nYour monthly payment = {0}".format(payment))
    else:
        payment += 1 
        last_paymment = principal - (count - 1) * payment
        print("\nYour monthly payment = {0} with last month payment = {1}".format(payment, last_paymment))