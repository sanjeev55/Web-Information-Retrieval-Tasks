from pyspark.sql import SparkSession


from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import *


conf = SparkConf().setAppName("Intelli_J").setMaster("local")
sc = SparkContext(conf=conf)

# spark = SparkSession.builder.appName("Intelli_J").master("local").getOrCreate()

# spark.read.format("csv").load("b.csv").show(10,False)


# titanic = spark.read.format("csv").load("Titanic.csv")
#
# print (titanic)

# rdd = spark.sparkContext.textFile('data.txt')

file = sc.textFile("data.txt")

lineLengths = file.map(lambda s: len(s))

print(lineLengths)

fileData = file.collect()

split12 = file.flatMap(lambda line: line.split(" "))

print(fileData)

# data = rdd.collect()


# print(data.flatMap(lambda line: line.split(" ")))
# data.flatMap(line: line.split(" "))
# txt.split(", ")

# rdd.flatMap(line=>line.split(" "))