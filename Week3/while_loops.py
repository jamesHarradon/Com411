noOfApplesToRemove = input("How many apples should I remove? ")
noOfApplesToRemoveInt = int(noOfApplesToRemove)
applesRemoved = 0

while applesRemoved < noOfApplesToRemoveInt:
    print("Removed apple.")
    applesRemoved += 1

obsToAvoid = input("How many obstacles must I avoid? ")
obsToAvoidInt = int(obsToAvoid)

noOfObs = 0

while noOfObs < obsToAvoidInt:
    print("Avoiding...", end="")
    noOfObs += 1
    print(f"Done {noOfObs} obstacles avoided!")


barsToChangeInt = int(input("How many bars should be charged? "))
noOfBarsCharged = 0
bar = "█ "

while noOfBarsCharged < barsToChangeInt:
    noOfBarsCharged += 1
    print("Charging:", end="")
    print(f"{noOfBarsCharged * bar}")
print("The battery is fully charged.")

phrase = input("Please enter a phrase: ")
print(phrase)
phraseLength = len(phrase)
while phraseLength > 0:
    print("Hi ", end="")
    phraseLength -= 1