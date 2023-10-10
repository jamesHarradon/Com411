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
