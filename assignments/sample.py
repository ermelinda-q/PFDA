# assignment_6_Weather.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the URL
url = "https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv"
data = pd.read_csv(url, skiprows=24)  # Skipping initial rows to get to the data

# Check column names to ensure we have the correct labels
print("Column names:", data.columns)

# Rename columns if necessary, or confirm the exact names
# Assuming the date column might have spaces around it, let's rename for consistency
data.columns = data.columns.str.strip()  # Strip any leading/trailing whitespace
data.rename(columns={'date': 'date', 'temp': 'temp'}, inplace=True)  # Adjust if names are different

# Convert the 'date' column to datetime format if it exists
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
else:
    print("Error: 'date' column not found.")
    exit(1)

# Plot: Temperature for each timestamp
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['temp'], color='blue', label='Hourly Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.legend()
plt.show()

# Calculate mean temperature each day
daily_mean_temp = data.groupby(data['date'].dt.date)['temp'].mean()

# Plot: Mean temperature each day
plt.figure(figsize=(10, 5))
plt.plot(daily_mean_temp.index, daily_mean_temp.values, color='orange', label='Daily Mean Temperature')
plt.xlabel('Date')
plt.ylabel('Mean Temperature (°C)')
plt.title('Mean Daily Temperature')
plt.legend()
plt.show()

# Calculate mean temperature for each month
monthly_mean_temp = data.groupby(data['date'].dt.to_period('M'))['temp'].mean()

# Plot: Mean temperature for each month
plt.figure(figsize=(10, 5))
plt.plot(monthly_mean_temp.index.astype(str), monthly_mean_temp.values, color='green', label='Monthly Mean Temperature')
plt.xlabel('Month')
plt.ylabel('Mean Temperature (°C)')
plt.title('Mean Monthly Temperature')
plt.xticks(rotation=45)
plt.legend()
plt.show()
