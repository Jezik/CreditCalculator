import math

command = input("What do you want to calculate?\ntype 'n' - for count of months,\ntype 'a' - for annuity monthly payment,\n" +
                "type 'p' - for credit principal:\n")
if command == "n":
    principal = int(input("Enter the credit principal:\n"))
    monthly_payment = float(input("Enter monthly payment:\n"))
    credit_interest = float(input("Enter credit interest:\n"))
    month_interest = credit_interest / 100 / 12
    period = math.log(monthly_payment / (monthly_payment - month_interest * principal), 1 + month_interest)
    period = math.ceil(period)
    years = period // 12
    months = period % 12
    print("You need {0} years and {1} months to repay the credit!".format(years, months))
elif command == "a":
    principal = int(input("Enter the credit principal:\n"))
    periods = int(input("Enter count of periods:\n"))
    credit_interest = float(input("Enter credit interest:\n"))
    month_interest = credit_interest / 100 / 12
    annuity_payment = principal * (month_interest * math.pow(1 + month_interest, periods) / (math.pow(1 + month_interest, periods) - 1))
    print("Your annuity payment = {0}!".format(math.ceil(annuity_payment)))
elif command == "p":
    monthly_payment = float(input("Enter monthly payment:\n"))
    periods = int(input("Enter count of periods:\n"))
    credit_interest = float(input("Enter credit interest:\n"))
    month_interest = credit_interest / 100 / 12
    principal = monthly_payment / (month_interest * math.pow(1 + month_interest, periods) / (math.pow(1 + month_interest, periods) - 1))
    print("Your credit principal = {0}!".format(math.floor(principal)))
else:
    print("Unknown command")