# Create an RDD from the df_salaries
rdd_salaries = df_salaries.rdd

# Collect and print the results
print(rdd_salaries.collect())

# Group by the experience level and calculate the maximum salary
dataframe_results = df_salaries.groupby("experience_level").agg({"salary_in_usd": 'max'})

# Show the results
dataframe_results.show()