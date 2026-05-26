import pandas as pd

file_path = 'data/TS.csv'
print(f"--- Checking unique values in the 'Year' column of {file_path} ---")

try:
    # We read the 'Year' column as a string to avoid errors
    df = pd.read_csv(file_path, dtype={'Year': str})

    # Get the unique values from the 'Year' column
    unique_years = df['Year'].unique()

    # Print the first 30 unique values to see the format
    print("Here are some of the unique values found:")
    print(unique_years[:30])

except Exception as e:
    print(f"An error occurred: {e}")