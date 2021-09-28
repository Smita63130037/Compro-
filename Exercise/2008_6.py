#SignificantConsant
tax_rate = 0.2
standart_deduction = 1500
deduction_per_dependent = 2500
#TheInput
gross_income = float(input("Enter gross income: "))
number_of_dependents = float(input("Enter number of dependent: "))
#Computation
net_income = gross_income - standart_deduction - (deduction_per_dependent * number_of_dependents)
income_tax = tax_rate * net_income
#Outputs
print(round(income_tax, 2))
