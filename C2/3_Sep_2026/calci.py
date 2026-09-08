def calci(a, b, choice):
    if choice == 1:
        print("Sum is = ", a + b)
    elif choice == 2:
        print("Subtraction is = ", a - b)
    elif choice == 3:
        print("Multiplication is = ", a * b)
    elif choice == 4:
        if b == 0:
            print("ZeroDivisionError: Cannot divide by zero!")
        else:
            print("Division is = ", a / b)

print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

try:
    choice = int(input("Enter Your Choice : "))
    if choice not in [1, 2, 3, 4]:
        print("Choice Error: Invalid option selected!")
    else:
        a = int(input("Enter 1st Value : "))
        b = int(input("Enter 2nd Value : "))
        calci(a, b, choice)

except ValueError:
    print("Operator Error!! or Value Error: Please enter numeric values only.")
