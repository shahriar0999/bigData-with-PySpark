# Define a Pandas UDF that adds 10 to each element in a vectorized way
@pandas_udf(DoubleType())
def add_ten_pandas(column):
    return column + 10

# Apply the UDF and show the result
df.withColumn("10_plus", add_ten_pandas(df['value']))
df.show()