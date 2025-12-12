import click
from pyspark_agentic_test.runner import AgenticRunner

@click.command()
@click.argument("module")
@click.option("--schema", default=None, help="Path to JSON schema.")
def run(module, schema):
    runner = AgenticRunner(module, schema_path=schema)
    results = runner.run()

    click.echo("\n=== PySpark Agentic Test Results ===")
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        click.echo(f"{status} — {name}")

if __name__ == "__main__":
    run()
