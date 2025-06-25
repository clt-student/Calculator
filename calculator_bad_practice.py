a = float(input("First #: "))
b = float(input("Second #: "))
c = input("Operation: ")

if c == "+":
    print("Sum is: " + str(a+b))

elif c == "-":
    print("Difference is: " + str(a-b))

elif c == "*":
    print("Product is: " + str(a * b))

elif c == "/":
    print("Division is: " + str(a/b))
    
else:
    print("Invalid operation. Please use +, -, *, or /.")