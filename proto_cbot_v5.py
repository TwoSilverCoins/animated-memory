import requests

# API endpoint
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Houston",
    "appid": "YOUR_API_KEY",  # Replace with your actual API key
    "units": "metric"
}

# Sending request
response = requests.get(weather_api_url, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    print(f"Current temperature in Houston: {temperature}°C")
else:
    print("Error fetching data.")

import requests

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_TOKEN = "YOUR_SECRET_TOKEN"
DATABASE_ID = "YOUR_DATABASE_ID"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Example task creation request
data = {
    "parent": {"database_id": DATABASE_ID},
    "properties": {
        "Title": {"title": [{"text": {"content": "Learn API Integration"}}]},
        "Status": {"select": {"name": "In Progress"}}
    }
}

response = requests.post(NOTION_API_URL, headers=headers, json=data)

if response.status_code == 200:
    print("Task successfully added to Notion!")
else:
    print("Failed to add task.")
