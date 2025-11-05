# Register the function age_category as a UDF
age_category_udf = udf(age_category, StringType())

# Apply your udf to the DataFrame
age_category_df_2 = age_category_df.withColumn("category", age_category_udf(age_category_df["age"]))

# Show df
age_category_df_2.show()