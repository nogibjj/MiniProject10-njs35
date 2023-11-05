## PySpark Data Processing MiniProject
This project focuses on leveraging PySpark for processing a large dataset. The primary goals include performing a data transformation and incorporating a Spark SQL query. To achieve this, I utilize a dataset from by fivethirtyeight, which contains information about Fandango movie reviews.

### Preparation:
1. Open codespaces
2. cd into the src directory
3. run: `python main.py`
4. View the logged output in the pyspark_output_data.md file.

### Makefile Recipes
1. Install dependencies: `make install`
1. Format code: `make format`
2. Lint code: `make lint`
3. Test code: `make test`

### Process
1. Begin by extracting the dataset using the extract function.
2. Initiate a Spark session using the start_spark function.
3. Load the dataset with the load_data function.
4. Perform a query on the dataset using the query function.
6. Transform the dataset using the transform function
7. Finally, end the Spark session using the teardown_spark function.