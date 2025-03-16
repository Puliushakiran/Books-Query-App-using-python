# Milestone II: Identifying the Most Stable City Based on Temperature Variance

import json
import pandas as pd
import requests
import datetime  # For handling date calculations

# Function to calculate temperature variance for a given city and date range
def get_temperature_variance(city, start_date, end_date):
    URL = 'https://api.oikolab.com/weather'
    OIKO_KEY = 'YOUR_OIKO_KEY_HERE'

    # API request to fetch temperature data
    resp = requests.get(URL,
        params={
            'param': ['temperature'],  # Requesting temperature data
            'start': start_date,       # Start date
            'location': city,          # City entered by the user
            'end': end_date,           # End date for a 7-day range
            'api-key': OIKO_KEY,       # Oikolab API key
            'freq': 'D'                # Frequency - Daily data
        }
    )

    # Extracting and formatting data
    weather_data = resp.json()['data']
    weather_data = json.loads(weather_data)

    # Creating a DataFrame to manage data efficiently
    df = pd.DataFrame(
        index=pd.to_datetime(weather_data['index'], unit='s'),
        data=weather_data['data'],
        columns=weather_data['columns']
    )

    # Calculating variance (spread of temperatures over 7 days)
    variance = df['temperature (degC)'].var()
    return variance

# Taking user input for cities and date
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")
start_date = input("Enter start date (YYYY-MM-DD): ")

# Converting the input date to a date object for easier manipulation
start_date = start_date.split('-')
obj1 = datetime.datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))

# Calculating end date by adding 7 days to the start date
obj2 = obj1 + datetime.timedelta(days=7)

# Formatting dates back to string format
start_date = obj1.strftime('%Y-%m-%d')
end_date = obj2.strftime('%Y-%m-%d')

# Calculating variance for both cities
var1 = get_temperature_variance(city1, start_date, end_date)
var2 = get_temperature_variance(city2, start_date, end_date)

# Comparing variance to decide the more stable city
if var1 < var2:
    print(f"We choose {city1} because it has less temperature variance.")
else:
    print(f"We choose {city2} because it has less temperature variance.")
