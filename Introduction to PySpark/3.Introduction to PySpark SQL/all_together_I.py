# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.appName('final_spark').getOrCreate()

# Print my_spark
print(my_spark)

# Load dataset into a DataFrame
df = my_spark.createDataFrame(data, schema=columns)


# Print my_spark
print(my_spark)

# Load dataset into a DataFrame
df = my_spark.createDataFrame(data, schema=columns)

df.show()