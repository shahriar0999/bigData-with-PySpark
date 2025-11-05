# Load the CSV file into a DataFrame
salaries_df = spark.read.csv("salaries.csv", header=True, inferSchema=True)

# Count the total number of rows
row_count = salaries_df.count()
print(f"Total rows: {row_count}")

# Group by company size and calculate the average of salaries
salaries_df.groupBy("company_size").agg({"salary_in_usd": "avg"}).show()
salaries_df.show()