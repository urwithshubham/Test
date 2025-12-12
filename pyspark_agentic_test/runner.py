import pandas as pd
import inspect
from pyspark_agentic_test.discovery import discover_functions
from pyspark_agentic_test.generator import TestCaseGenerator
from pyspark_agentic_test.spark_fixture import get_spark

class AgenticRunner:
    def __init__(self, module, schema_path=None):
        self.module = module
        self.spark = get_spark()

        if schema_path:
            import json
            with open(schema_path) as f:
                self.schema = json.load(f)
        else:
            self.schema = None

    def run(self):
        funcs = discover_functions(self.module)
        if not funcs:
            raise ValueError("No PySpark functions found in module.")

        gen = TestCaseGenerator(self.spark, self.schema)

        df = gen.from_schema() if self.schema else gen.synthetic()

        results = []
        for fn in funcs:
            expected = fn(df)
            result = fn(df)

            exp_pdf = expected.orderBy(expected.columns).toPandas()
            res_pdf = result.orderBy(result.columns).toPandas()

            results.append((fn.__name__, exp_pdf.equals(res_pdf)))

        return results
