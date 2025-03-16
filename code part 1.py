# Milestone I: Fetch Weather Data for a Specific Date

import json
import pandas as pd
import requests

# Taking city name and date as input
city = input("Enter city: ")
date = input("Enter date (YYYY-MM-DD): ")

# API endpoint and API key (Replace with your Oikolab API Key)
URL = 'https://api.oikolab.com/weather'
OIKO_KEY = 'YOUR_OIKO_KEY_HERE'

# Sending request to the API
resp = requests.get(URL,
    params={
        'param': ['temperature'],  # Requesting temperature data
        'start': date,             # Starting date
        'location': city,          # City entered by the user
        'end': date,               # Same as start date (for a single day)
        'api-key': OIKO_KEY,       # Oikolab API key
        'freq': 'D'                # Frequency - Daily data
    }    
)

# Extracting and formatting the response data
weather_data = resp.json()['data']
weather_data = json.loads(weather_data)

# Creating a DataFrame to handle the data
df = pd.DataFrame(
    index=pd.to_datetime(weather_data['index'], unit='s'), 
    data=weather_data['data'], 
    columns=weather_data['columns']
)

# Extracting the temperature value from the DataFrame
temp = int(df.iloc[0, 4])  # Extracting the first row's temperature value

# Displaying the result
print(f"Temperature for {city} on {date} = {temp}°C")
