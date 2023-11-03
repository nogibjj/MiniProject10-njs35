from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr


spark = SparkSession.builder.appName("Week10MiniProject").getOrCreate()
df = spark.read.csv("data.csv", header=True, inferSchema=True)


# Apply a transformation (filtering)
filtered_df = df.filter(col("some_column") > 10)

# Perform a Spark SQL query
df.createOrReplaceTempView("temp_table")
result_df = spark.sql("SELECT AVG(some_column) FROM temp_table")

