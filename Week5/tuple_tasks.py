# tuples are immutable and use () brackets

def likelihood():
    likelihoods  =(50, 38, 27, 99, 4)
    return min(likelihoods)

def run_task1():
    val = likelihood()
    print(f"Minimum likelihood of falling: {val}%")

#the function is only called when the file is executed directly and not when it is imported into another module.
if __name__ == "__main__":
    run_task1()


# below function returns two values using a tuple
def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


# if a function returns a tuple, you can assign the values to two variables
def run_task2():
    minVal, maxVal = likelihood_min_max()
    print(f"Minimum likelihood of falling: {minVal}%")
    print(f"Maximum likelihood of falling: {maxVal}%")

run_task2()