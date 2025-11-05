# Examine the data
airports.show()

# .withColumnRenamed() renames the "faa" column to "dest"
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on='dest', how='leftouter')

# Examine the new DataFrame
flights_with_airports.show()