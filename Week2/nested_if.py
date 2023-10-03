cover_type = input("Enter book cover type, hard or soft: ")

if cover_type == "soft":
    is_perfect_bound = input("Is the book Perfect Bound? ")
    if is_perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    elif is_perfect_bound == "no":
        print("Soft covers with coils or stitches are great for short books")
    else:
        print("Please enter yes or no")
elif cover_type == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("Please enter either hard or soft")


# find your phone


found_phone = False

while found_phone == False:
    where_to_look = input("Where should I look? ")
    if where_to_look == "bedroom":
        where_in_bedroom = input("Where should I look in the bedroom? ")
        if where_in_bedroom == "under bed":
            print("Found some shoes but no phone")
        else:
            print("Found some mess but no phone")
    elif where_to_look == "bathroom":
        where_in_bathroom = input("Where should I look in the bathroom? ")
        if where_in_bathroom == "in bath":
            print("Found a rubber duck but no phone")
        else:
            print("Found bathroom stuff but no phone")
    elif where_to_look == "living room":
        where_in_living_room = input("Where should I look in the living room? ")
        if where_in_living_room == "on the table":
            print("Yes! I found my phone!")
            found_phone = True
        else:
            print("Found some stuff but no phone")
    else:
        print("I do not know where that is but I will keep looking...")