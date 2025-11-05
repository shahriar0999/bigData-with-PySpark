# Load the dataframe
census_df = spark.read.json("adults.json")

# Filter rows based on age condition
salary_filtered_census = census_df.filter(census_df['age'] > 40)

# Show the result
salary_filtered_census.show()