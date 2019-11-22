from __future__ import print_function
import sys
from operator import add
from pyspark import SparkContext
from pyspark.sql import SparkSession
import json
from csv import reader

if __name__ == "__main__":
    sc = SparkContext()
    spark = SparkSession \
        .builder \
        .appName("final-project") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    # load table into database
    table = spark.read.format('csv')\
        .options(delimiter="\t",header='true',inferschema='true')\
        .load(sys.argv[1])
    table.createOrReplaceTempView("table") # create table
    fileName = sys.argv[2] # the name of the dataset correlating to the tsv file
    inFile = sys.argv[1].split('.',1)[0]
    print ("profiling file:" + fileName) # print output message

    columns = {} # a list of columns
    keycandidates={} # all the columns that could be primary key candidates

    # go through the table and for each column, create the column_specification content
    tcp_interactions = spark.sql("select * from table")
    tcp_interactions.show()
    cols = tcp_interactions.columns # array of all column names
    for col in cols: # for each column
        column = {}
        ##########################################################################
        # TODO: this is the place where you guys write your code
   
        column['column_name'] = col # the name of the column
        # TODO: get the number of non empty cells (type: integer)
        column['number_non_empty_cells'] = "placeholder"
        # TODO: get the numebr of empty cells (type: integer)
        column['number_empty_cells'] = "placeholder"
        # TODO: number of distinct values in the column (type: integer)
        column['number_distinct_values'] = "placeholder"
        # TODO: top 5 most frequent values of this column(type: array)
        column['frequent_values'] = "placeholder"

        # all the data types in this column
        data_types=[]
        # TODO: for every data type that this column have, output the required values in data_types
        # this might require a map_reduce job

        column['data_types'] = data_types
        columns[col] = column

    # assembling the json file
    data = {} # the base for the json file
    data['dataset_name'] = fileName # assign dataset_name value to the json file
    data['columns'] = columns # assign columns value to the json file
    data['key_column_candidates'] = keycandidates # assign key_column_candidates to the json file
    
    # write the json file to output, name the output file as inFile.json, inFile being the name of the file
    inFile = inFile.split("/")
    inFile = inFile[len(inFile)-1]
    outputFile = inFile+".json"
    with open(outputFile, 'w+') as outfile:
        json.dump(data, outfile)
    sc.stop()
