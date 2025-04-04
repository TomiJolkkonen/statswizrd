from pyspark.sql import SparkSession
import json

HDFS_INPUT = "/user/hadoop/la_kings_stats/raw_data.json"
HDFS_OUTPUT = "/user/hadoop/la_kings_stats/cleaned_data.parquet"

spark = SparkSession.builder.appName("TransformLAKingsData").getOrCreate()

# Read JSON from HDFS
df = spark.read.json(HDFS_INPUT)

# Convert values to proper types (modify as needed)
df = df.withColumnRenamed("_1", "Stat").withColumnRenamed("_2", "Value")

# Write cleaned data back to HDFS as Parquet
df.write.parquet(HDFS_OUTPUT, mode="overwrite")

print("Data transformation complete.")
