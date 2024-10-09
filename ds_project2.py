import pandas as pd
import matplotlib.pyplot as plt

unemployment_df = pd.read_csv(r'C:\Users\dhina\Downloads\india.csv')

# Explore the dataset
print(unemployment_df.head())
print(unemployment_df.info())

# Check for leading/trailing spaces in column names
print("Columns:", unemployment_df.columns.tolist())  # Print the list of column names

# Clean column names by stripping spaces
unemployment_df.columns = unemployment_df.columns.str.strip()

# Now convert date column to datetime format
unemployment_df['Date'] = pd.to_datetime(unemployment_df['Date'])  # Convert to datetime
unemployment_df.set_index('Date', inplace=True)  # Set as index

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(unemployment_df['Estimated Unemployment Rate (%)'], label='Unemployment Rate', color='blue')
plt.title('Unemployment Rate Over Time in India')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
