import pandas as pd

series = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("Example Series from Pandas: \n", series)

data = {"Name": ["Alice", "Bob"], "Age": [45, 34]}
print("Example data frame from Pandas: \n", pd.DataFrame(data))

# Common Loading Data Methods
# CSV, Excel, or a dictionary

# Read from a file
csv_data = pd.read_csv("data/employee_details.csv")

# Save to a file without index column
csv_data.to_csv("data/employee_details1.csv", index=False)
csv_data.to_excel("data/employee_details.xlsx", index=False)

# Viewing Data
print("PRINT the first 5 rows: \n", csv_data.head())
# print("Print the last 3 rows: \n", csv_data.tail())
print("PRINT the information/metadata of the data: \n", csv_data.info())
print("DESCRIBE the data set: \n", csv_data.describe())
print("PRINT mulitple columns: Name and Age column: \n", csv_data[["Name", "Age"]])
print("PRINT data where age is > 25: \n", csv_data[csv_data["Age"] > 25])
print("PRINT the first row by position 0: \n", csv_data.iloc[0])
print("PRINT the first column by postion 0: \n", csv_data.iloc[:, 0])