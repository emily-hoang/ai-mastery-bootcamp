import matplotlib.pyplot as plt

x = [1990, 2000, 2019, 2025]
y = [5, 6, 7, 8]

# Line Plot
plt.plot(x, y, marker='o')
plt.title("Basic Line Plot")
plt.xlabel("Year")
plt.ylabel("Population in Billion")
plt.tight_layout()
plt.show()

# Bar Chart
plt.bar(x, y)
plt.title("Basic Bar Chart")
plt.xlabel("Year")
plt.ylabel("Population in Billion")
plt.tight_layout()
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("Year")
plt.ylabel("Population in Billion")
plt.tight_layout()
plt.show()

# Histogram (we'll plot the years — typically hist is used for distributions)
plt.hist(x, bins=4, edgecolor='black')
plt.title("Basic Histogram")
plt.xlabel("Year")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Pie Chart (use population values)
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=140)
plt.title("Population Distribution by Year")
plt.tight_layout()
plt.show()
