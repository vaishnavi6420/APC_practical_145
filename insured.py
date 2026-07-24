marital_status = input("Enter marital status (married/unmarried): ").lower()
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if marital_status == "married":
    print("The driver is insured.")
elif marital_status == "unmarried":
    if gender == "male" and age > 30:
        print("The driver is insured.")
    elif gender == "female" and age > 25:
        print("The driver is insured.")
    else:
        print("The driver is not insured.")
else:
    print("Invalid marital status entered.")
