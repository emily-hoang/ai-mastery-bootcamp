import pandas as pd

employees = pd.DataFrame({
  "EmployeeID": [101, 102, 103, 104],
  "Name": ["Alex", "Marry", "David", "Charles"],
  "Department": ["HR", "IT", "Finance", "Security"]
})
print("PRINT employee data: \n", employees)

salaries = pd.DataFrame({
  "EmployeeID": [101, 102, 103, 104],
  "Salary": [7000, 5000, 80000, 4000]
})
print("PRINT salaries data: \n", salaries)

# merging data
merged_data = pd.merge(employees, salaries, on="EmployeeID", how="inner")
print("PRINT merged employees and salaries data: \n", merged_data)
# concatenation data
concat_data = pd.concat([employees, salaries], ignore_index=True)
print("PRINT concatenated employees and salaries data: \n", concat_data)
# joining data
employees_indexed = employees.set_index("EmployeeID")
salaries_indexed = salaries.set_index("EmployeeID")
joined_data = employees_indexed.join(salaries_indexed, how="left")
print("PRINT joined employees and salaries on EmployeeID: \n", joined_data)
