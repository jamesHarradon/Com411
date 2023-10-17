print("Program Started!")
c = input("Please enter a standard character: ")

if len(c) == 1:
    code = ord(c)
    print(f"The ASCII code for {c} is {code}")
else:
    print("Please enter a single character")

print("Program Ended!")


print("Program Started!")
code = input("Please enter an ASCII code: ")

codeNum = abs(int(code))

if codeNum in range(32, 126):
    c = chr(codeNum)
    print(f"The character represented by the ASCII code {codeNum} is {c}")
else:
    print("Please enter a ASCII code between 32 and 126")