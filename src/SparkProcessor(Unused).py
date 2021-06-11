import pyspark as ps            #Spark
import pyspark.sql.types as types
import pyspark.sql.functions as f
import psycopg2 as pg2          #Postgres
from pymongo import MongoClient #MongoDB   # is this needed

#udf functions
def c():
    pass

class SparkProcessor():
    '''
    Pull scraped data from Mongo, clean it and return it to postgres, as well as make sub tables in postgres showing information such as total incomplete records per feature
    '''
    def __init__(self):
        self.spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("Craigslist_EDA") \
            .getOrCreate()


    def Register_UDFS(self):
        colsInt = f.udf(lambda z: c(z), types.IntegerType())
        self.spark.udf.register("colsInt", colsInt)
        pass
    def callUDF_Example(self):
        df2 = self.df.withColumn( 'semployee',self.spark.colsInt('employee'))
        pass
    def LoadFromMongo(self):
        self.df = self.spark.read.format("mongo").option("uri", "mongodb://127.0.0.1/craigslist.all_listings").load()
        self.df.createOrReplaceTempView('listings')

    def RunColumns(self):
        for n in self.df.schema.names:
            print(n)
        #self.df.schema.fields
        pass
    def CheckForNulls(self):
        
        
        pass
    def CheckForZeroes():
        
        pass
    def CheckForEmpties():

        pass
    def ConvertTypes():
        pass
    def CheckForOutliers():
        pass
    def CleanStringToNumber(self,cols):
        for c in cols:
            self.df.withColumn(c, f.regexp_replace('Animal', ))
        pass 
    def RunQuery():
        pass
    def ToPandas():
        pass