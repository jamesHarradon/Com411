import csv

def read_csv(file_path):
    with open(file_path) as file:
        # reads csv file, saves in variable
        csv_reader = csv.reader(file)
        # next function gets first line of file (headings), using next again will grab next line of csv
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print(f"Values:")
        for values in csv_reader:
            print(values)

def run_task1():
    read_csv("clothing.csv")

# executes function when the file is executed directly
if __name__ == "__main__":
  run_task1()


def extract(file_path):
    print("Extracting...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n"
    print("Done! The extracted items are as follows:")
    print(names)

def run_task2():
    extract("clothing.csv")
    
run_task2()

