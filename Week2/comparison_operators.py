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


num_string1 = input("Please input a number: ")
num1 = int(num_string1)
num_string2 = input("Please input a second number: ")
num2 = int(num_string2)
num_string3 = input("Please input a third number: ")
num3 = int(num_string3)

countOfOdd = 0
countOfEven = 0

if num1 % 2 == 0:
    countOfEven += 1
else:
    countOfOdd += 1



if num2 % 2 == 0:
    countOfEven += 1
else:
    countOfOdd += 1

if num3 % 2 == 0:
    countOfEven += 1
else:
    countOfOdd += 1

print(f"There were {countOfEven} even and {countOfOdd} odd numbers.")