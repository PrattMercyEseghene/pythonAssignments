number1 = int(input("Enter first number : "))

operator = (input("Enter any of this operators(*,+,-,/): "))[0]

number2 = int(input("Enter second number: "))

if(operator == ("+")):
    sum = number1 + number2
    print(sum)
    
if(operator ==("-")):
    difference = number1 - number2
    print(difference)
        
if(operator == ("*")):
    multiplication = number1 * number2
    print(multiplication)
    
if(operator == ("/")):

    division = number1 / number 2
    print(division)
