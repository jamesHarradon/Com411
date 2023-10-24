def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def run_task1():
    print(directions())


# the below code ensures that the function is only called when the file is executed directly
# and not when it is imported into another module
if __name__ == "__main__":
    run_task1()



def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    path = movements()
    for x in range(0, len(path), 2):
        print(f"{path[x]} for {path[x+1]} steps")



run_task2()

def menu():
    print("Please select a direction: ")
    list = directions()
    for i in range(len(list)):
        print(f"{i}: {list[i]}")

def run_task3():
    menu()

run_task3()