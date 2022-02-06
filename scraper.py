import requests
import json

url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "cache-control": "max-age=0",
    "sec-ch-ua": "^\^Chromium^^;v=^\^92^^, ^\^"
}

response = requests.request("GET", url, data=payload, headers=headers)

#print(response.text)
jsondata=json.loads(response.text)

for game in jsondata['events']:
    league=game['tournament']['name']
    hometeam=game['homeTeam']['name']
    awayteam=game['awayTeam']['name']
    #print(hometeam,'-',awayteam)
    homescore=game['homeScore']['current']
    awayscore=game['awayScore']['current']
    
    print(league,'|',hometeam,homescore,'-',awayscore,awayteam)
