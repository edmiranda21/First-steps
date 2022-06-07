import argparse
import math
import sys

year = 12
percent = 100


# To calculate the number of periods
def n_months(principal, m_payment, interest):
    nominal_interest = float(interest / (year * percent))
    # calculate the number of payments in months
    payment = math.ceil(math.log(m_payment / (m_payment - nominal_interest * principal), (1 + nominal_interest)))
    n_year = payment // year
    months = payment % year
    overpayment = payment * m_payment - principal
    if n_year > 1:
        if months < 1:
            print(f'It will take {n_year} years to repay this loan')
        if months > 1:
            print(f'It will take {n_year} years and {months} months to repay this loan')
        if months == 1:
            print(f'It will take {n_year} years and {months} month to repay this loan')
    else:
        if months > 1:
            print(f'It will take {months} months to repay this loan')
        else:
            print(f'It will take {months} month to repay this loan')
    print(f'Overpayment = {overpayment}')


# to calculate the loan principal
def loan_principal(annuity, periods, interest):
    nominal_interest = float(interest / (year * percent))
    loan = math.floor(annuity / ((nominal_interest * math.pow((1 + nominal_interest), periods)) /
                                 (math.pow((1 + nominal_interest), periods) - 1)))
    overpayment = round(periods * annuity - loan)
    print(f'Your loan principal = {loan}!')
    print(f'Overpayment = {overpayment}')


# to calculate the annuity payment
def annuity_payment(loan, periods, interest):
    nominal_interest = float(interest / (year * percent))
    payment = math.ceil(loan * ((nominal_interest * math.pow((1 + nominal_interest), periods)) /
                                (math.pow((1 + nominal_interest), periods) - 1)))
    print(f'Your monthly payment = {payment}!')
    overpayment = round(payment * periods - loan)
    print(f'Overpayment = {overpayment}')


# to calculate diff months
def d_month(principal, periods, interest):
    overpayment = 0
    nominal_interest = float(interest / (year * percent))
    for m in range(1, periods + 1, 1):
        d_month = math.ceil((principal / periods) + nominal_interest * (principal - (principal * (m - 1) / periods)))
        print(f'Month {m}: payment is {d_month}')
        overpayment = overpayment + d_month
    if overpayment - principal < 0:
        pass
    else:
        print('Overpayment: ', overpayment - principal)


# argparse module
parser = argparse.ArgumentParser()

# parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

# to use user input
args = parser.parse_args()

# parameters numbers
p_arguments = [args.payment, args.principal, args.periods, args.interest]


# to calculate positive numbers
def negative_number(p_arguments):
    for number in p_arguments:
        if number is None:
            pass
        else:
            if number < 0:
                print("Incorrect parameters")


if len(sys.argv) <= 4:
    print("Incorrect parameters")
elif args.type is None or args.interest is None:
    print("Incorrect parameters")
else:
    # to calculate the differentiated payments
    if args.type == 'diff':
        if args.periods is None or negative_number(p_arguments):
            print("Incorrect parameters")
        else:
            d_month(args.principal, args.periods, args.interest)
    # to calculate not differentiated payments
    if args.type == 'annuity':
        # to calculate the loan principal
        if args.principal is None or negative_number(p_arguments):
            loan_principal(args.payment, args.periods, args.interest)
        # to calculate the periods payment
        elif args.periods is None or negative_number(p_arguments):
            n_months(args.principal, args.payment, args.interest)
        # to calculate the monthly payment
        else:
            annuity_payment(args.principal, args.periods, args.interest)
