#!/bin/bash
module load python/gnu/3.6.5
module load spark/2.4.0 

hdfs dfs -get /user/hm74/NYCOpenData/datasets.tsv
list=$(hdfs dfs -ls /user/hm74/NYCOpenData/*.gz)
i=0
for item in $list; do
        verify=$(echo $item|grep .tsv.gz)
        if [ $verify ]; then
                i=$((i+1))
                if [ $i -lt 951 ]; then
                        continue;
                fi
		if [ $i -gt 1902 ]; then
			break;
		fi
                echo " this is the $i file"
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
