
import pyspark
from pyspark import SparkConf

from pyspark.sql.connect.session import SparkSession

sample_dict = {
    "file1": {"key1": "value1", "key2": "value2", "key3": "value3"},
    "file2": {"key1": "value4", "key2": "value5", "key3": "value6"}
}
print(sample_dict)

spark = SparkSession.builder.getOrCreate()
df = spark.createDataFrame(sample_dict)
df.show()
