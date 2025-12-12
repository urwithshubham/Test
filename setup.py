from setuptools import setup, find_packages

setup(
    name="pyspark-agentic-test",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyspark-agent-test=pyspark_agentic_test.cli:run",
        ]
    },
    install_requires=[
        "pyspark",
        "pytest",
        "click"
    ],
)
