import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        global headings
        headings = next(csv_reader)
        for values in csv_reader:
            records.append(values)
    print("Done!")

def display_menu():
    choice = input("Please select one of the following options:\n[1] Display all passenger names\n[2] Display number of surviving passengers\n[3] Display number of passengers per gender\n[4] Display number of passengers per age group\n")
    choice_int = int(choice)
    return choice_int

def display_passenger_names():
    print("The names of the passengers are: ")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)

def display_num_survivors():
    num_survived = 0
    for record in records:
        if record[1] == '1': num_survived += 1
    print(f"{num_survived} passengers survived.")   


def display_passengers_per_gender():
    males = 0
    females = 0
    for record in records:
        if record[4] == "male": males += 1
        if record[4] == "female": females += 1
    print(f"{males} males, {females} females")  

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        age = record[5]
        if age == "": continue
        # float here because there are decimal ages for some reason - you can convert string float/int to float but not to int.
        age_float = float(age)
        if age_float < 18: children += 1
        elif age_float < 65: adults += 1
        else: elderly += 1      
    print(f"{children} children, {adults} adults, {elderly} elderly")

def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")
    if selected_option == 1: 
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    else:
        print("Error! Option not recognised")

run()


