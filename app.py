import requests

api_key = "657e010d70fc40b6951bb7865f3953a2"
api_url = f"https://api.sportsdata.io/v3/nba/scores/json/AreAnyGamesInProgress?key={api_key}"

response = requests.get(api_url)

print(response.json())
