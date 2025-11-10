# Register as a view
df.createOrReplaceTempView("data_view")

# Advanced SQL query: Calculate total salary by Position
result = spark.sql("""
    SELECT Position, SUM(Salary) AS Total_Salary
    FROM data_view
    GROUP BY Position
    ORDER BY Total_Salary DESC
    """
)
result.show()