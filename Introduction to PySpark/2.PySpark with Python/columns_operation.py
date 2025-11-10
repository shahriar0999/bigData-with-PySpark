# Create a new column 'weekly_salary'
census_df_weekly = census_df.withColumn('weekly_salary', census_df['income']/52)

# Rename the 'age' column to 'years'
census_df_weekly = census_df_weekly.withColumnRenamed('age', 'years')

# Show the result
census_df_weekly.show()