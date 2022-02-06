import json
with open("Scores.json") as f:
    jsondata=json.load(f)


#print(jsondata)
#league=jsondata['events'][0]['tournament']['name']
#print(league)
hometeam=jsondata['events'][0]['homeTeam']['name']
awayteam=jsondata['events'][0]['awayTeam']['name']
#print(hometeam,'-',awayteam)
homescore=jsondata['events'][0]['homeScore']['current']
awayscore=jsondata['events'][0]['awayScore']['current']

#print(league,'|',hometeam,homescore,'-',awayscore,awayteam)

for game in jsondata['events']:
    league=game['tournament']['name']
    hometeam=game['homeTeam']['name']
    awayteam=game['awayTeam']['name']
    #print(hometeam,'-',awayteam)
    homescore=game['homeScore']['current']
    awayscore=game['awayScore']['current']
    
    print(league,'|',hometeam,homescore,'-',awayscore,awayteam)

