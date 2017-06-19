
# Debt Caclulator

# Write a program to calculate the remaining balance after one year if a person
# pays only the minimum montly payment required each month. Add interest on the
# remaining balance each month.

def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):

    monthlyInterestRate = annualInterestRate / 12.0

    for i in range(12):
        balance -= (balance * monthlyPaymentRate)
        balance += (balance * monthlyInterestRate)
        # print("Month {} remaining balance is {:0.2f}".format(i + 1, balance))

    print("Remaining Balance: {}".format(round(balance, 2)))

remainingBalance(balance = 484, annualInterestRate = 0.2, monthlyPaymentRate = 0.04)
