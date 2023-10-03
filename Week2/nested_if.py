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