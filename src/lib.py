"""
Useful functions for the project
"""
import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    FloatType,
)
from pyspark.sql.functions import col, when

OUTPUT_FILE = "../pyspark_output_data.md"


def log_output_data(operation_type, data_output, input_query=None):
    """
    Log the output data to a file
    """
    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(f"{operation_type} operation\n")
        if input_query:
            file.write(f"{input_query}\n")
        file.write("See data output below: \n")
        file.write(data_output)
        file.write("\n\n\n")


def build_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark


def extract(
    csv_url="https://github.com/fivethirtyeight/data/raw/master/fandango/fandango_scrape.csv",
    save_file_path="fandango_scrape.csv",
):
    """
    Extract csv data from url
    """
    with requests.get(csv_url, timeout=100) as r:
        with open(save_file_path, "wb") as f:
            f.write(r.content)
    return save_file_path


def load_data(spark, data_path="fandango_scrape.csv"):
    """
    Load the extracted csv data into pyspark
    """
    schema = StructType(
        [
            StructField("FILM", StringType(), True),
            StructField("STARS", IntegerType(), True),
            StructField("RATING", FloatType(), True),
            StructField("VOTES", IntegerType(), True),
        ]
    )
    spark_dataframe = spark.read.option("header", "true").schema(schema).csv(data_path)
    log_output_data("LOAD", spark_dataframe.limit(5).toPandas().to_markdown())
    return spark_dataframe


def query(spark, spark_df, input_query, name):
    """
    SQL query via spark
    """
    spark_df = spark_df.createOrReplaceTempView(name)
    log_output_data("QUERY", spark.sql(input_query).toPandas().to_markdown(), input_query)
    return spark.sql(input_query).show()


def transform(spark_df):
    """
    Perform a set data transformation on the data.
    Specifically, add a new column to the dataframe called "Low_Vote_High_Rating".
    This column indicates if the movie has a high rating but a low total
    number of votes.
    """
    spark_df = spark_df.withColumn(
        "Low_Vote_High_Rating",
        when((col("RATING") > 4.0) & (col("VOTES") < 25), 1).otherwise(0),
    )

    log_output_data("TRANSFORM", spark_df.limit(5).toPandas().to_markdown())

    return spark_df.show()


def teardown_spark(spark):
    spark.stop()
    return True
