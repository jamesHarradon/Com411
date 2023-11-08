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

def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")

run()