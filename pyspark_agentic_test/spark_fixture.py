from pyspark.sql import SparkSession

def get_spark():
    return (
        SparkSession.builder
        .master("local[*]")
        .appName("pyspark-agentic-test")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
