print("1 Addition")
print("2 Substraction")
print("3 Multiplication")
print("4 Division")

option = int(input("Enter the Option : "))

a = float(input("Enter First Value : "))
b = float(input("Enter Second Value : "))

if option == 1:
    print("Addition is = ", a+b )
elif option == 2:
    print("Substraction is = ", a-b)
elif option == 3:
    print("Multiplication is = ", a*b)
elif option == 4:
    print("Division is = ", a/b)
else:
    print("Invalid Option")