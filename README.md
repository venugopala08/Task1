# Task1


I performed a complete data cleaning process on the sales_data_sample.csv file using Pandas in Google Colab. Here's what I did:

Uploaded the dataset into the Colab environment.

Read the CSV file using the 'latin1' encoding to handle special characters properly.

Previewed the first few rows to get an initial look at the dataset.

Checked the structure and data types of all columns using .info().

Identified missing values in each column with .isnull().sum().

Dropped rows that had more than two missing values to maintain data quality.

Filled remaining missing values using forward fill to ensure continuity.

Found and removed duplicate rows to avoid redundancy.

Stripped extra spaces from column names for consistency.

Converted the ORDERDATE column to a proper datetime format for easier date-based analysis.

Previewed the cleaned dataset and confirmed the final structure and types
