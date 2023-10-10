# noOfApplesToRemove = input("How many apples should I remove? ")
# noOfApplesToRemoveInt = int(noOfApplesToRemove)
# applesRemoved = 0
#
# while applesRemoved < noOfApplesToRemoveInt:
#     print("Removed apple.")
#     applesRemoved += 1
#
# obsToAvoid = input("How many obstacles must I avoid? ")
# obsToAvoidInt = int(obsToAvoid)
#
# noOfObs = 0
#
# while noOfObs < obsToAvoidInt:
#     print("Avoiding...", end="")
#     noOfObs += 1
#     print(f"Done {noOfObs} obstacles avoided!")
#
#
# barsToChangeInt = int(input("How many bars should be charged? "))
# noOfBarsCharged = 0
# bar = "█ "
#
# while noOfBarsCharged < barsToChangeInt:
#     noOfBarsCharged += 1
#     print("Charging:", end="")
#     print(f"{noOfBarsCharged * bar}")
# print("The battery is fully charged.")
#
# # len function - finds length of string
#
# phrase = input("Please enter a phrase: ")
# print(phrase)
# phraseLength = len(phrase)
# while phraseLength > 0:
#     print("Hi ", end="")
#     phraseLength -= 1

# Calculate the sum of the first 100 numbers

print("Calculating the sum of the first 100 numbers...")

num = 0
total = 0

while num < 101:
    total += num
    num += 1
print(f"Done! The answer is {total}")
















