num_string1 = input("Please input a number: ")
num1 = int(num_string1)
num_string2 = input("Please input a second number: ")
num2 = int(num_string2)

if num1 > num2:
    print("The second number is the smallest!")
elif num1 < num2:
    print("The first number is the smallest!")
else:
    print("Both numbers are equal!")