#Calculator
print("+")
print("-")
print("*")
print("/")
print("%")
#input
operator = input("select operator: ")
number_1 = float(input("Enter number: "))
number_2 = float(input("Enter number: "))
if operator == "+":
    print("=", str(number_1+number_2))
elif operator == "-":
    print("=", str(number_1-number_2))
elif operator == "*":
    print("=", str(number_1*number_2))
elif operator == "/":
    print("=", str(number_1/number_2))
elif operator == "/":
    if number_2 == 0:
        print("error")
    else:
        print("=", str(number_1/number_2))
elif operator == "%":
    if number_2 == 0:
        print("error")
    else:
        print("=", str(number_1%number_2))