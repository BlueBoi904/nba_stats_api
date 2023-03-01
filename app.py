import requests
import os

# Set environment variables
# os.environ['API_USER'] = 'username'
# os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
api_key = os.getenv('API_KEY')

api_url = f"https://api.sportsdata.io/v3/nba/scores/json/AreAnyGamesInProgress?key={api_key}"

response = requests.get(api_url)

print(response.json())
