import requests
import os

# Set environment variables
# os.environ['API_USER'] = 'username'
# os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
api_key = os.getenv('API_KEY')
season = '2023'
team = 'ORL'

url_base = "https://api.sportsdata.io/v3/nba/scores/json"
url_extension = f"/Players/{team}?key={api_key}"

response = requests.get(url_base + url_extension)
# Response returns a list of dict with info pertaining to each player on a team.
data = response.json()

for item in data:
    if item["PlayerID"]:
        print(item["PlayerID"])
    if item["YahooName"]:
        print(item["YahooName"])
