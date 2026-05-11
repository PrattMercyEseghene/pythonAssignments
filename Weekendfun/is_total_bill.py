#5. Discount Eligibility :  Ask for total_bill and is_member ("yes" or "no"). Apply discount: ● If total_bill >= 1000 and is_member == "yes" → 10% off ● If total_bill >= 1000 but not member → 5% off ● Else → No discount Print final amount and discount message


total_bill=float(input("Enter total bill:"))

is_member= input("Are you a member? (yes/no):")

discount = 0.0


if total_bill >= 1000.0:
    if(is_member == "yes"):
#        discount = 0.10
        print("discount applied is : 10%")
    
    if(is_member == "no"):
    
#        discount = 0.5
    
        print("discount applied is: 5%")
    
else:

    print("no discount")
