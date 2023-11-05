"""
Main
"""
from lib import (
    build_spark,
    extract,
    load_data,
    teardown_spark,
    query,
    transform
)


def main():
    """
    ETL using pyspark.
    All outputs are logged to pyspark_output_data.md
    """
    # Extract the data from the csv file
    extract()

    # Create the spark session
    spark = build_spark("Fandango")

    # Load the data into pyspark
    spark_df = load_data(spark)

    # Run an example query. Find the average rating for films with more than 100 votes
    query(
        spark,
        spark_df,
        "SELECT AVG(RATING) FROM Fandango WHERE VOTES > 100",
        "Fandango",
    )

    # Preform an example transformation. Add a new column to detect possibly misleading ratings
    spark_df = transform(spark_df)

    # Teardown spark
    teardown_spark(spark)


if __name__ == "__main__":
    main()
