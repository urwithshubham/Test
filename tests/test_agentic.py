from pyspark_agentic_test.runner import AgenticRunner

def test_agentic():
    runner = AgenticRunner("src.transformations", schema_path="tests/schema.json")
    results = runner.run()
    for name, passed in results:
        assert passed, f"{name} failed"
