import math
import argparse


def calculate_principal(monthly_payment, periods, credit_interest):
    month_interest = credit_interest / 100 / 12
    principal = monthly_payment / (month_interest * math.pow(1 + month_interest, periods) / (math.pow(1 + month_interest, periods) - 1))
    return math.floor(principal)

def calculate_period(principal, monthly_payment, credit_interest):
    month_interest = credit_interest / 100 / 12
    period = math.log(monthly_payment / (monthly_payment - month_interest * principal), 1 + month_interest)
    period = math.ceil(period)
    years = period // 12
    months = period % 12
    return (years, months)

def calculate_payment(principal, periods, credit_interest):
    month_interest = credit_interest / 100 / 12
    payment = principal * (month_interest * math.pow(1 + month_interest, periods) / (math.pow(1 + month_interest, periods) - 1))
    return math.ceil(payment)

def calculate_diff_payment(principal, periods, credit_interest, cur_period):
    month_interest = credit_interest / 100 / 12
    payment = principal / periods + month_interest * (principal - principal * (cur_period - 1) / periods)
    return math.ceil(payment)

def calculate_overpayment(payments, principal):
    return int(payments - principal)

parser = argparse.ArgumentParser(description="Credit calculator")
parser.add_argument("type", choices=["annuity", "diff"], help="type of payment")
parser.add_argument("--principal", type=int, help="principal of a credit")
parser.add_argument("--periods", type=float, help="number of months to pay")
parser.add_argument("--interest", type=float, help="credit interest")
parser.add_argument("--payment", type=float, help="monthly payment")
args = parser.parse_args()
print()

if args.type == "annuity":
    if args.periods and args.interest and args.payment:
        if args.periods > 0 and args.interest > 0 and args.payment > 0:
            principal = calculate_principal(args.payment, args.periods, args.interest)
            print("Your credit principal = {}!".format(principal))
            print("Overpayment = {}".format(calculate_overpayment(args.periods * args.payment, principal)))
        else:
            print("Incorrect parameters. Parameters must be positive.")
    elif args.principal and args.interest and args.payment:
        if args.principal > 0 and args.interest > 0 and args.payment > 0:
            years, months = calculate_period(args.principal, args.payment, args.interest)
            if months > 0:
                print("You need {0} years and {1} months to repay the credit!".format(years, months))
            else:
                print("You need {} years to repay the credit!".format(years))
            print("Overpayment = {}".format(calculate_overpayment((years * 12 + months) * args.payment, args.principal)))
        else:
            print("Incorrect parameters. Parameters must be positive.")
    elif args.principal and args.periods and args.interest:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            payment = calculate_payment(args.principal, args.periods, args.interest)
            print("Your annuity payment = {}!".format(payment))
            print("Overpayment = {}".format(calculate_overpayment(args.periods * payment, args.principal)))
        else:
            print("Incorrect parameters. Parameters must be positive.")            
    else:
        print("Incorrect parameters. Run with '-h' key to get help.")
elif args.type == "diff":
    if args.principal and args.periods and args.interest:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            total_payment = 0
            for i in range(int(args.periods)):
                payment = calculate_diff_payment(args.principal, args.periods, args.interest, i + 1)
                total_payment += payment
                print("Month {0}: paid out {1}".format(i + 1, payment))
            print("\nOverpayment = {}".format(calculate_overpayment(total_payment, args.principal)))
        else:
            print("Incorrect parameters. Parameters must be positive.")  
    else:
        print("Incorrect parameters. Run with '-h' key to get help.")
