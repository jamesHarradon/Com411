import tui

def list_years(data):
    tui.started()
    years = set()
    for row in data:
        years.add(row[9])
    list_years = list(years)
    list_years.sort()
    list_years.reverse()
    tui.display_years(list_years)
    tui.completed()

def tally_medals(data):
    tui.started()
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for row in data:
        medal = row[14]
        if medal == "NA": continue
        medals[medal] += 1
    tui.display_medal_tally(medals)
    tui.completed()

def tally_team_medals(data):
    tui.started()
    team_medals = {}
    for values in data:
        medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
        team = values[6]
        medal = values[14]
        if medal == "NA": continue
        if (team in team_medals.keys()):
            team_medals[team][medal] += 1
        else:
            medals[medal] += 1
            single_team = {team: medals}
            team_medals.update(single_team)
    tui.display_team_medal_tally(team_medals)
    tui.completed()

    
   
            

