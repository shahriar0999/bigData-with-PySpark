# Cache the DataFrame
df.cache()

# Perform aggregation
agg_result = df.groupBy("Department").sum("Salary")
agg_result.show()

# Analyze the execution plan
agg_result.explain()

# Uncache the DataFrame
df.unpersist()