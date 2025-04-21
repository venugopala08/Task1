import pandas as pd
from google.colab import files

# Step 1: Upload the CSV file
uploaded = files.upload()

# Step 2: Load the file with appropriate encoding 
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Step 3: Preview the raw data
print(" First 5 rows of raw data:")
display(df.head())

# Step 4: Basic structure and data types
print("\n Dataset Info:")
df.info()

# Step 5: Check for missing values
print("\n Missing values per column:")
print(df.isnull().sum())

# Step 6: Drop rows with too many missing values 
df = df.dropna(thresh=len(df.columns) - 2) 

# Step 7: Fill remaining missing values 
df.fillna(method='ffill', inplace=True)

# Step 8: Remove duplicate rows
duplicates = df.duplicated().sum()
print(f"\n🧹 Duplicate rows found: {duplicates}")
df = df.drop_duplicates()

# Step 9: Clean column names 
df.columns = df.columns.str.strip()

# Step 10: Fix formatting — convert dates, numerical values etc.
if 'ORDERDATE' in df.columns:
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')


# Step 11: Final check
print("\n Cleaned Data Preview:")
display(df.head())

print("\n Final Data Info:")
df.info()
