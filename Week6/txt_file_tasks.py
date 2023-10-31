import os
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():
    print("Processing...")
    cwd()

#run()


def display_chars(file_path, no_of_chars_to_be_read):
    with open(file_path) as file:
        data = file.read(no_of_chars_to_be_read)
        print(f"The first {no_of_chars_to_be_read} characters are:")
        print(data)

def display_line(file_path):
    with open(file_path) as file:
        line = file.readline()
        print(line)

def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)

def run_task2():
    display_chars("library.txt", 6)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run_task2()