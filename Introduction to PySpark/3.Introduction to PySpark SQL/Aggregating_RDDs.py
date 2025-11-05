# DataFrame Creation
data = [("HR", "3000"), ("IT", "4000"), ("Finance", "3500")]
columns = ["Department", "Salary"]
df = spark.createDataFrame(data, schema=columns)

# Map the DataFrame to an RDD
rdd = df.rdd.map(lambda row: (row["Department"], row["Salary"]))

# Apply a lambda function to get the sum of the DataFrame
rdd_aggregated = rdd.reduceByKey(lambda x, y: x + y)

# Show the collected Results
print(rdd_aggregated.collect())