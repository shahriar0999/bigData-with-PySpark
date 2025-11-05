# Drop rows with any nulls
census_cleaned = census_df.na.drop()

# Show the result
census_cleaned.show()