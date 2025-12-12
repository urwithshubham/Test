import json
from pyspark.sql import Row

class TestCaseGenerator:
    def __init__(self, spark, schema=None):
        self.spark = spark
        self.schema = schema

    def from_schema(self):
        rows = [Row(**row) for row in self.schema["data"]]
        return self.spark.createDataFrame(rows)

    def synthetic(self, n=5):
        if self.schema and "data" in self.schema:
            cols = list(self.schema["data"][0].keys())
        else:
            cols = ["id", "value"]
        rows = [Row(**{c: i for c in cols}) for i in range(n)]
        return self.spark.createDataFrame(rows)
