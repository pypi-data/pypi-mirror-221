import os
from databricks.sdk.runtime import *
from pyspark.sql import SparkSession

def autoloader(mount_location, date_str, file_format, options):
    dbfs_mount_location = f"{mount_location}"
    date_path = os.path.join(dbfs_mount_location, date_str)

    if not dbutils.fs.ls(date_path):
        print(f"Error: Data for date '{date_str}' not found in mount location '{mount_location}'.")
        return None

    spark = SparkSession.builder.appName("DataLoader").getOrCreate()
    if file_format == 'csv':
        data = spark.read.option("header", "true").csv(date_path, **(options or {}))
    elif file_format == 'parquet':
        data = spark.read.parquet(date_path)

    return data