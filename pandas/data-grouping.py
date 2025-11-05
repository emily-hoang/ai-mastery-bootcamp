import pandas as pd

data = pd.read_csv("data/employee_details.csv")
print("PRINT original data: \n", data)
print("CHECKING for missing values: \n", data.isnull().sum())

# Group data by name and loop through each row to print the data
grouped_name_data = data.groupby("Name")

for name, group in grouped_name_data:
  print("NAME data: \n", name)
  print("GROUP data: \n", group)
  
# Multi Aggregation (Average, Min, Max) With Data Grouped By Name (If the same name repeats, it will shows the average, min, max values)
sales_data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'UnitsSold': [10, 15, 14, 8, 20, 5, 12, 10],
    'Revenue': [1000, 1500, 1400, 800, 2000, 500, 1200, 1000]
})
grouped_region_data = sales_data.groupby("Region")
grouped_region_aggregated_data = grouped_region_data.agg({"Revenue":["mean", "max", "min"]})
print("AGGREGATION: AVERAGE, MAX, MIN value in grouped data by age: \n", grouped_region_aggregated_data)

average_revenue_data = grouped_region_data["Revenue"].mean()
print("PRINT average revenue data: \n", average_revenue_data)
max_revenue_data = grouped_region_data["Revenue"].max()
print("PRINT max revenue data: \n", max_revenue_data)
min_revenue_data = grouped_region_data["Revenue"].min()
print("PRINT min revenue data: \n", min_revenue_data)

pivoted_data = data.pivot_table(
  values="Age",
  index="Name",
  aggfunc="mean"
)
print("PIVOTTED DATA: \n", pivoted_data)