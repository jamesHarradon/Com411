import matplotlib.pyplot as plt

def display_line(x, y):
    plt.plot(x,y)
    plt.show()

def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)

run_task1()

def small():
    x_values = [3, 3, 4, 4, 3]
    y_values = [3, 4, 4, 3, 3]
    plt.plot(x_values, y_values, "or--")
    plt.show()

small()

def medium():
