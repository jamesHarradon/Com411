string_num = input("Please enter a whole number: ")

num = int(string_num)

if num % 2 == 0:
    print("The number is an even number")
elif num % 2 != 0:
    print("The number is an odd number")