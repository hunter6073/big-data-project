Instructions:
run the profiling job requires the following steps:
1. in dataset_index.txt, only save the lines of files that are assigned to you and haven't ran yet. By default, it contains all the files that need to be profiled.
    - You can achieve this by using Util/remaining_task_generate.py. It will generate a file in remaining_data/ folder. You can use that file as your dataset_index.txt in the root directory (if the process fails).
    - The file should look like this :
```
16, '/user/hm74/NYCOpenData/2abb-gr8d.tsv.gz', 'HOME-STAT Weekly Dashboard'
17, '/user/hm74/NYCOpenData/2anc-iydk.tsv.gz', '2015-16 Health Education HS Data - City Council District'
...
```

2. run the command: 
$ module load spark/2.4.0
$ module load python/gnu/3.6.5
$ spark-submit task1.py 0 1900

3. Task1.py will generate one profiled json file per dataset in the raw_output/ folder. You can use Util/task1_json_generator.py to generate the final deliverable json file saved as deliverable/task1.json
    - The output format of the deliverable is a list of json files
```
[
{dataset 1},
{dataset 2},
...
]
```