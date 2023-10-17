print("Program Started!")
c = input("Please enter a standard character: ")

if len(c) == 1:
    code = ord(c)
    print(f"The ASCII code for {c} is {code}")
else:
    print("Please enter a single character")

print("Program Ended!")