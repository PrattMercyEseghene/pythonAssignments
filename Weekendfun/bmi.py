height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kg:"))

discount = 0


bmi = weight / (height * height)

print("your bmi is :", bmi)


if bmi < 18.5:

    print("underweight")
    
elif 18.5<= bmi <= 24.9:

    print("normal")
    
elif 25 <= bmi <= 29.9:

    print("overweight")
    
else:

    print("obese")


#total_bill = float(input("Enter total bill:"))
#
#is_member = input("Are you a member? (yes/ no):")
#
#if total_bill >= 1000 :
#
#    if is_member == "yes" :
#    
#        discount = 0.10
#    
#        print("discount applied is: 10%")
#
#
#else:
#
#    discount = 0.05
#
#    print("discount applied is: 5%")
#
#else:
#
#print("no discount")
#
#
