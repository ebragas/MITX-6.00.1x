"""
# Debt Caclulator

# Write a program to calculate the remaining balance after one year if a person
# pays only the minimum montly payment required each month. Add interest on the
# remaining balance each month.
"""

def minPayment(balance, annualInterestRate):
    """
    Input: balance, as int or float for loan balance; annualInterestRate, as float for interest rate

    Returns the minimum constant monthly payment to pay off the loan in 12 months.
    """

    monthlyInterestRate = annualInterestRate / 12.0

    lowerBound = round(balance / 12.0, 2)
    upperBound = round((balance * (1 + monthlyInterestRate)**12) / 12.0, 2)

    while True:
        payment = (upperBound + lowerBound) / 2
        tempBalance = balance

        for i in range(12):
            tempBalance -= payment
            tempBalance += tempBalance * monthlyInterestRate

        # print("Payment: {} Balance: {}".format(payment, round(tempBalance, 2)))

        if round(tempBalance, 2) == 0:
            print("Lowest Payment: {}".format(round(payment, 2)))
            return
        elif tempBalance > 0:
            lowerBound = payment
        else:
            upperBound = payment

# minPayment(balance, annualInterestRate)
minPayment(320000, 0.2)
