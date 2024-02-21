#!/usr/bin/python3
"""
Purpose: Compound Interest

    Compound Interest : A = P(1 + r/n)nt

                        A = Accured amount (principal + interest)
                        P = Principal amount
                        r = Annual nominal interest rate as a decimal
                        R = Annual nominal interest rate as a percent
                        r = R/100
                        n = number of compounding periods per unit of time
                        t = time in decimal years; e.g., 6 months is calculated as 0.5 years. Divide your partial year number of months by 12 to get the decimal years.

ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php                        


"""

principal_amount = float(input("Enter the Principal Amount : "))
annual_rate = float(input("Enter the Annual_rate " ))/100
compound = float(input("Enter No of times Compounded per year :"))
time = float(input("Enter Time : "))

Accured_Amount = round(principal_amount * (1+(annual_rate/compound))**(compound*time), 2)

print("Total Amount :", Accured_Amount)
print("Total Interest = ", round((Accured_Amount - principal_amount), 2))

