# Create a DataFrame
df = spark.read.csv("salaries.csv", header=True, inferSchema=True)

# Convert DataFrame to RDD
rdd = df.rdd

# Show the RDD's contents
rdd.collect()
print(rdd)