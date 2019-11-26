#!/bin/bash
module load python/gnu/3.6.5
module load spark/2.4.0 

min=$1
max=$2
if [ -z ${min} ];then
exit 0
fi
if [ -z ${max} ];then
exit 0
fi
input="dataset_index.txt"
while IFS= read -r line
do
	index=$(echo $line | cut -d "," -f1) # the index
	fileName=$(echo $line | cut -d "," -f2) # Name of the file
	datasetName=$(echo $line | cut -d "," -f3) # Name of the dataset
	if [ $index -ge $min ] && [ $index -lt $max ]; then
		fileName=$(echo $fileName | tr "'" '"')
		datasetName=$(echo $datasetName | tr "'" '"')
		spark-submit test.py $fileName "$datasetName"
	fi
done < "$input"

echo "all jobs started, check ps for background process display"
