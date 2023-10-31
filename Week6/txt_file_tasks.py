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

# run()


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

# add the following code to the end of your file so that it executes the function run_task2 when the file is executed directly.
# if __name__ == "__main__":
#     run_task2()


def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for line in file:
            print(f"Looked in: {line}")
            print("...Done!")

def run_task3():
    search("library.txt")

# run_task3()



def search_books(file_path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line + "\n"
            else:
                books += line + "\n"
        print("Done!")
    return f"{sections}\n\n{books}"

def save(file_path, data):
    print("Saving...")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")

def run_task4():
    data = search_books("books.txt")
    save("section-books.txt", data)

run_task4()