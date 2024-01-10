from pyspark.sql import SparkSession

from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql.types import ArrayType, DoubleType, BooleanType, DateType
from pyspark.sql.functions import col, split, substring, when, to_date, format_number, avg


def init_spark():
  sql = SparkSession.builder\
    .appName("myapp")\
    .config("spark.jars", "/opt/spark-apps/postgresql-42.2.22.jar")\
    .getOrCreate()
  sc = sql.sparkContext
  return sql,sc


def main():
  schema = StructType() \
    .add('number', IntegerType(), True) \
    .add('property_type', StringType(), True) \
    .add('price', DoubleType(), True) \
    .add('location', StringType(), True) \
    .add('city', StringType(), True) \
    .add('baths', IntegerType(), True) \
    .add('purpose', StringType(), True) \
    .add('bedrooms', IntegerType(), True) \
    .add('Area_in_Marla', DoubleType(), True)

  # connect to db
  url = "jdbc:postgresql://demo-database:5432/price_data"
  properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
  }

  # path to csv file
  file = "/opt/spark-data/house_prices.csv"
  sql,sc = init_spark()

  # read csv file 
  df = sql.read.option('header', True)\
            .option("quote", "\"")\
            .option("escape", "\"")\
            .schema(schema)\
            .csv(file)

  df.groupBy('location', 'bedrooms')\
            .agg(avg(col('price'))\
            .alias('AVGPrice'))\
            .withColumn('AVGPrice', format_number(col('AVGPrice'),2))\
            .sort('location', 'bedrooms')\
            .show(df.count(), truncate=False)

  
if __name__ == '__main__':
  main()