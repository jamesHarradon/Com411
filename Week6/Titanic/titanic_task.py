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
    choice = input("Please select one of the following options:\n[1] Display all passenger names\n[2] Display all surviving passengers\n[3] Display number of passengers per gender\n[4] Display number of passengers per age group\n")
    choice_int = int(choice)
    return choice_int

def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")

run()



