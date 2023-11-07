import csv

def read_csv(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")



read_csv("clothing.csv")