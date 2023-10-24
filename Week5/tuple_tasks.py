# tuples are immutable and use () brackets

def likelihood():
    likelihoods  =(50, 38, 27, 99, 4)
    return min(likelihoods)

def run_task1():
    val = likelihood()
    print(f"Minimum likelihood of failling: {val}%")

#the function is only called when the file is executed directly and not when it is imported into another module.
if __name__ == "__main__":
    run_task1()

