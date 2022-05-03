print ("What equation type will you be peforming")
print("Adding")
print("Subtracting")
print("Multiplying")
print("Dividing")
operation = int(input())
if operation == 1:
    num1 = input("First Number ")
    num2 = input ("Second Number ")
    print ("The sum is " + str(int(num1) + int(num2)))
elif operation == 2:
    num1 = input("First Number ")
    num2 = input ("Second Number ")
    print("The sum is " + str(int(num1) - int(num2)))
elif operation == 3:
    num1 = input("First Number ")
    num2 = input ("Second Number ")
    print("The sum is " + str(int(num1) * int(num2)))
elif operation == 4:
    num1 = int(input("First Number "))
    num2 = int(input ("Second Number "))
    print("The sum is " + str(int(num1) / int(num2)))
else:
    print("INVALID ENTRY")
