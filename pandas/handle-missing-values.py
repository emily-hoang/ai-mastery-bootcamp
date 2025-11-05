import pandas as pd

data = pd.read_csv("data/missing_rows_employee_details.csv")
print("PRINT original data: \n", data)

# Drop rows with missing values
clean_rows_data = data.dropna()
print("DROP rows with missing value: \n", clean_rows_data)
# Drop column with missing values
clean_columns_data = data.dropna(axis=1)
print("DROP columns with missing value: \n", clean_columns_data)

# Fill Name column with value Nil if missing
data["Name"] = data["Name"].fillna("Nil")

# Forward fill propagates the last known non-null value forward to fill the missing (NaN) values.
missing_data = {'Value': [1, None, None, 4, None]}
df = pd.DataFrame(missing_data)
print("PRINT original data: \n", df)

df_ffill = df.ffill()
print("PRINT foward filled data: \n", df_ffill)

# Backward fill propagates the next known non-null value backward to fill in the blanks.
df_bfill = df.bfill()
print("PRINT backward filled data: \n", df_bfill)

# Interpolation "guesses" missing values based on patterns in your data — usually using linear, polynomial, or other curve-fitting methods.
# Linear interpolation (default)
df_interp = df.interpolate()
print("PRINT interpolated data with linear method: \n", df_interp)