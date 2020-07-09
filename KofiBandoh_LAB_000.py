##Simple Calculator to operate on three numbers

def add(a,b,c):
    return a + b + c

def subtract(a, b, c):
    return a - b - c

def multiplication(a, b, c):
    return a*b*c

def divide (a, b, c):
    return (a/ b/ c )

print("Welcome to calculator \n "  )
print("Select: \n1 for addition \n2 for subtraction \n3 for multiplication \n4 for subtraction ")

while True:
    operator = int(input("Enter operation number: "))

    if operator in (1, 2, 3, 4):
        a = int(input("Enter number: "))
        b = int(input("Enter another number:" ))
        c = int(input("Enter the last number: "))

        if operator == 1:
            print("Your answer is:" , add(a, b, c))

        elif operator == 2:
            print("Your answer is:", subtract(a, b, c))

        elif operator == 3:
            print("Your answer is:", mutiplication(a, b, c))

        elif operator == 4:
            print("Your answer is:", divide(a, b, c))

        break

    else:
        print("Invalid operator input ")