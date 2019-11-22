#!/bin/bash
module load spark/2.2.0
module load python/gnu/3.4.4
# TODO: for every file in the folder, find its corresponding name through dataset.tsv, then
# put the file name and dataset name in the command below
############## single file for testing ####################
# hdfs dfs -put cspg-yi7g.tsv.gz testfile
# spark-submit test.py cspg-yi7g.tsv.gz testfile

############# final output ############################
hdfs dfs -get /user/hm74/NYCOpenData/datasets.tsv
list=$(hdfs dfs -ls /user/hm74/NYCOpenData/*.gz)
for item in $list; do
	verify=$(echo $item|grep .tsv.gz)
	if [ $verify ]; then
		# verify is the address of the public dataset
		echo $verify
		# needs to chagne from /user/hm74/NYCOpenData/ywiv-5gyw.tsv.gz to ywiv-5gyw
		foo=${verify%".tsv.gz"}
		foo=$(echo $foo | sed 's!/user/hm74/NYCOpenData/!!')
		ds_name=$(grep $foo datasets.tsv)
		ds_result=$(echo ${ds_name//$foo/})
		spark-submit test.py "$verify" "$ds_result"
	fi
done
