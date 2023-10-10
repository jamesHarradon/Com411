# numOfMountains = int(input("How many mountains should I display?"))
#
# print("Displaying...")
#
# for count in range(numOfMountains):
#     print("     __")
#     print("    /  \_ ")
#     print("   /^    \\")
#     print("  /  ^    \_")
#     print("_/ ^ ^     ^\\")
#     print("/  ^     ^    \\")
#
# print("Done!")
#
# # Count down
#
#
# howFar = int(input("How far are we from the target? "))
# print(howFar)
#
# for count in range(howFar, 0, -1):
#     print(f"{count} steps remaining")
#
# print("Target achieved!")
#
# # cheat way
# howFar = int(input("How far are we from the target? "))
# print(howFar)
#
# for count in range(howFar):
#     print(f"{howFar - count} steps remaining")
#
# print("Target achieved!")

# Range

level = int(input("What level of brightness is required?"))
print(level)
x = "*"

print("Adjusting brightness...")
for count in range(2, level, 2):
    print(f"Brightness level: {x * count}")