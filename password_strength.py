password = input("Enter password: ")[0]

if(password < "6"):
    print("weak")
    
elif(password > "10"):
    print("Strong")
    
elif (password > "6" and password <= "10"):
    print("medium")
    
else:
    print("invalid input")


