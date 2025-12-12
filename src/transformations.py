from pyspark.sql.functions import col

def clean_users(df):
    return df.filter(col("active") == True).select("id", "name")
