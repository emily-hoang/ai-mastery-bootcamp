import pandas as pd

data = pd.read_csv("data/employee_details.csv")
print("PRINT original data: \n", data)

data = data.rename(columns={"Name": "Full Name"})
print("PRINT modified Name column to Full Name: \n", data)

data["Age"] = data["Age"].astype("float")
print("PRINT modified data type for Age from int to float: \n", data)

data["YearsExperience"] = pd.to_datetime(data["YearsExperience"])
print("PRINT modified YearsExperience to datetime format: \n", data)

data["FutureSalary"] = data["Salary"] * 2
print("PRINT Adding a new column of double of Salary: \n", data)