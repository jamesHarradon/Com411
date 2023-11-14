def dashes():
    dashes = ""
    for i in range(85):
        dashes += "-"
    return dashes

def started(msg=""):
    print(dashes())
    print(f"Operation started: {msg}...\n")

def completed():
    print("\nOperation completed")
    print(dashes())

def error(msg):
    print(f"Error! {msg}")

def menu():
    print("Please select one of the following options:")
    menu_display = '''
    [years]      List unique years
    [tally]      Tally up medals
    [ctally]     Tally up medals for each team
    [exit]       Exit the program
    
    '''
    selection = input(menu_display)
    print(f"Your selection: {selection}")

menu()