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
    [team]       Tally up medals for each team
    [exit]       Exit the program
    '''
    print(menu_display)
    selection = input()
    print(dashes())
    print(f"Your selection: {selection}")
    return selection

def display_medal_tally(tally):
    for key, value in tally.items():
        print(f"|{key:<10}| {value:<10}|")

def display_team_medal_tally(team_tally):
    for key, values in team_tally.items():
        name = key
        medals = values
        print("\n" + name)
        for key, value in medals.items():
            print(f"|{key:<10}| {value:<5}|")

def display_years(years):
    for year in years:
        print(year)

