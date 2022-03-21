def nba_cup(result_sheet, to_find):
    teams = ["Los Angeles Clippers", "Dallas Mavericks", "New York Knicks", "Atlanta Hawks", "Indiana Pacers",
            "Memphis Grizzlies", "Los Angeles Lakers", "Minnesota Timberwolves", "Phoenix Suns", "Portland Trail Blazers",
            "New Orleans Pelicans", "Sacramento Kings", "Houston Rockets", "Denver Nuggets", "Cleveland Cavaliers", "Milwaukee Bucks",
            "Oklahoma City Thunder", "San Antonio Spurs", "Boston Celtics", "Philadelphia 76ers", "Brooklyn Nets", "Chicago Bulls",
            "Detroit Pistons", "Utah Jazz", "Miami Heat", "Charlotte Hornets", "Toronto Raptors", "Orlando Magic", "Washington Wizards",
            "Golden State Warriors"]
    match_ups = result_sheet.split(",")
    team_match_ups = []
    wins = 0
    draws = 0
    losses = 0
    points_scored = 0
    points_against = 0
    standings_points = 0
    
    if not to_find:
        return ''
    if to_find not in teams:
        return f"{to_find}:This team didn't play!"
    
    for match_up in match_ups:
        if to_find in match_up:
            team_match_ups.append(match_up)
            
    for team_match_up in team_match_ups:
        entry = team_match_up.replace(to_find,'').lstrip().split()
        
        if entry[0].isalpha():
            while entry[0].isalpha():
                entry.remove(entry[0])

            if '.' in entry[0] or "." in entry[-1]:
                return f"Error(float number):{team_match_up}"
            elif int(entry[0]) == int(entry[-1]):
                draws += 1
                points_scored += int(entry[0])
                points_against += int(entry[-1])
            elif int(entry[0]) < int(entry[-1]):
                wins += 1
                points_scored += int(entry[-1])
                points_against += int(entry[0])
                standings_points += 3
            else:
                losses += 1
                points_scored += int(entry[-1])
                points_against += int(entry[0])
        else:
            if '.' in entry[0]:
                return f"Error(float number):{team_match_up}"
            elif int(entry[0]) == int(entry[-1]):
                draws += 1
                points_scored += int(entry[0])
                points_against += int(entry[-1])
            elif int(entry[0]) > int(entry[-1]):
                wins += 1
                points_scored += int(entry[0])
                points_against += int(entry[-1])
                standings_points += 3
            else:
                losses += 1
                points_scored += int(entry[0])
                points_against += int(entry[-1])

    
    return f"{to_find}:W={wins};D={draws};L={losses};Scored={points_scored};Conceded={points_against};Points={standings_points}"