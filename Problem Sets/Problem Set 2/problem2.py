
# Debt Caclulator

# Write a program to calculate the remaining balance after one year if a person
# pays only the minimum montly payment required each month. Add interest on the
# remaining balance each month.

def minPayment(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPayment = 0

    while True:
        monthlyPayment += 10
        tempBalance = balance

        # Calculate balance over 12 months
        for i in range(12):
            tempBalance -= monthlyPayment
            tempBalance += tempBalance * monthlyInterestRate

        # print("Payment: {} Balance: {}".format(monthlyPayment, tempBalance))

        if tempBalance <= 0:
            print("Lowest Payment: {}".format(monthlyPayment))
            return

# minPayment(3926, 0.2)
minPayment(balance, annualInterestRate)
