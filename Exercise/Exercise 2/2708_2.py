#Vaccine

first_dose = input("Enter first vaccine (sv,az,si,none): ")
second_dose = input("Enter second vaccine (sv,az,si,none): ")
third_dose = input("Enter third vaccine (sv,az,si,none): ")
infected = input("Have you got infected? (yes,no): ")
if first_dose == "sv" and second_dose == "sv" and third_dose == "none":
    print("pz=1")
elif first_dose == "si" and second_dose == "si" and third_dose == "none":
    print("pz=1")
elif first_dose == "sv" and second_dose == "none" and third_dose == "none":
    print("pz=1")
elif first_dose == "az" and second_dose == "none" and third_dose == "none":
    print("pz=1")
elif first_dose == "si" and second_dose == "none" and third_dose == "none":
    print("pz=1")
elif first_dose == "none" and second_dose == "none" and third_dose == "none":
    if infected == "yes":
        print("pz=1")
    elif infected == "no":
        print("pz=2")
elif first_dose == "sv" and second_dose == "sv" and third_dose == "az":
    print("none")
elif first_dose == "sv" and second_dose == "az" and third_dose == "none":
    print("none")
elif first_dose == "az" and second_dose == "az" and third_dose == "none":
    print("none")
