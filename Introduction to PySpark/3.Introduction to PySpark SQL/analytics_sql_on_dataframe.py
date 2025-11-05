# Create a temporary view of salaries_table
salaries_df.createOrReplaceTempView('salaries_table')

# Construct the "query"
query = '''SELECT job_title, salary_in_usd FROM salaries_table WHERE company_location == "CA"'''

# Apply the SQL "query"
canada_titles = spark.sql(query)

# Generate basic statistics
canada_titles.describe().show()