# Weather App Using Python

This Weather App fetches real-time weather data from the internet and provides insights into specific locations' weather conditions. The app is designed to analyze data and determine the most stable city based on temperature variance.

---

## Project Overview
This application allows users to:
- Fetch real-time weather data for any given city and date.
- Analyze temperature variance across multiple cities to identify the most stable location.
- Utilize data visualization tools for improved insights.

---

## Features
- Fetches weather data using **Oikolab Weather API**.
- Uses **JSON** format for data retrieval and parsing.
- Employs **Pandas** for efficient data manipulation and analysis.

---

## Tools & Technologies
- **Python** (Core language)
- **APIs** (For data retrieval)
- **JSON** (For structured data exchange)
- **Pandas** (For data manipulation)

---

## Prerequisites
Before running this project, ensure you have the following:
- Python installed (Version 3.8 or above recommended)
- Required libraries:
  - `requests`
  - `pandas`

To install the dependencies, run:
```bash
pip install requests pandas
```

---

## Oikolab API Setup
1. Visit [Oikolab](https://oikolab.com) and create an account.
2. Generate your API key.
3. Replace `'YOUR_OIKO_KEY_HERE'` in the code with your API key.

---

## Project Structure
```
📂 WeatherApp
 ├── 📄 milestone1.py
 ├── 📄 milestone2.py
 ├── 📄 requirements.txt
 ├── 📄 README.md
```

---

## Milestone I: Fetch Weather Data for a Specific Date
### Description
In this milestone, the program accepts:
- **City Name** (e.g., Hyderabad)
- **Date** (e.g., 2024-03-01)  

It then fetches the temperature data for the given date from the **Oikolab Weather API** and displays the temperature in Celsius.

### Code Explanation
1. **Imports**:  
   - `json` for parsing data.
   - `pandas` for organizing data in tabular form.
   - `requests` for sending API requests.

2. **Input**:  
   - The user is prompted to enter a **city name** and a **date**.

3. **API Request**:  
   - The code sends a `GET` request to the Oikolab API with parameters like:
  - `param`: Specifies data type (e.g., temperature).
  - `start` and `end`: The date for which data is requested.
  - `location`: The city name entered by the user.
  - `'api-key'`: The API key for authentication.

4. **Data Processing**:  
   - The received JSON data is parsed and loaded into a Pandas DataFrame.
   - The relevant temperature value is extracted and displayed.

### Sample Input/Output
```
Enter city: Hyderabad
Enter date (YYYY-MM-DD): 2024-03-01
Temperature for Hyderabad on 2024-03-01 = 32°C
```

---

## Milestone II: Find the Most Stable City
### Description
In this milestone, the program accepts:
- **Two city names** (e.g., Delhi and Mumbai).
- **Start date** for weather observation.  

The program calculates the **temperature variance** for each city over a 7-day period and recommends the city with the most stable weather.

### Code Explanation
1. **Imports**:  
   - `json`, `pandas`, and `requests` for data handling.
   - `datetime` to manipulate dates.

2. **Function: `get_temperature_variance()`**  
   - This function sends an API request similar to Milestone I but fetches data for 7 days.
   - The variance in temperature values is calculated using Pandas' `.var()` method.
   - The variance value is returned.

3. **Date Calculation**:  
   - The user enters a start date.  
   - The program automatically calculates the **end date** by adding 7 days to the start date.

4. **Comparison Logic**:  
   - The variance values for both cities are compared.
   - The city with the **lower variance** is considered the most stable city.

### Sample Input/Output
```
Enter first city: Delhi
Enter second city: Mumbai
Enter start date (YYYY-MM-DD): 2024-03-01
We choose Mumbai because of less temperature variance
```

---

## How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/Puliushakiran/Weather-App-Python.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Add your Oikolab API key inside the `milestone1.py` and `milestone2.py` files.
4. Run the desired milestone file:
```bash
python milestone1.py
```
OR
```bash
python milestone2.py
```

---

## Future Enhancements
- Add graphical weather visualizations using `matplotlib`.
- Implement additional weather parameters like humidity, wind speed, etc.
- Introduce a user-friendly GUI for better interaction.

---

## Troubleshooting
- **API Error**: Ensure the API key is valid and entered correctly.
- **Data Not Found**: Verify the city name and date format.
- **Library Error**: Reinstall the required libraries by running:
```bash
pip install -r requirements.txt
```

