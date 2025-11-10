# Create a temporary table "people"
df.createOrReplaceTempView("people")

# Select the names from the temporary table people
query = """SELECT name FROM people"""

# Assign the result of Spark's query to people_df_names
people_df_names = spark.sql(query)

# Print the top 10 names of the people
people_df_names.show(10)