Instructions:
run the file require 2 steps:
1. in dataset_index.txt, only save the lines of files that are assigned to you and haven't ran yet.

You can achieve this by using Util/remaining_task_generate.py. It will generate a file in remaining_data folder. You can use that file as your dataset_index.txt

it should look like this :

16, '/user/hm74/NYCOpenData/2abb-gr8d.tsv.gz', 'HOME-STAT Weekly Dashboard'
17, '/user/hm74/NYCOpenData/2anc-iydk.tsv.gz', '2015-16 Health Education HS Data - City Council District'
18, '/user/hm74/NYCOpenData/2ay5-tqqe.tsv.gz', '2015-2016 Local Law 14 Health Data - MS District'
19, '/user/hm74/NYCOpenData/2bef-phhy.tsv.gz', '2016 - 2017 Computer Science Report'
20, '/user/hm74/NYCOpenData/2bh6-qmgg.tsv.gz', '2006-2012 Math Test Results - Citywide - Gender'
21, '/user/hm74/NYCOpenData/2bmr-jdsv.tsv.gz', 'FHV Base Aggregate Report - Historical'
22, '/user/hm74/NYCOpenData/2bnn-yakx.tsv.gz', 'Parking Violations Issued - Fiscal Year 2017'
23, '/user/hm74/NYCOpenData/2cmn-uidm.tsv.gz', 'Capital Commitment Plan'
24, '/user/hm74/NYCOpenData/2dzy-e7cu.tsv.gz', '2016 - 2017 Health Education Report'
25, '/user/hm74/NYCOpenData/2ei9-vg68.tsv.gz', 'NYCHA Application Priority Codes'
26, '/user/hm74/NYCOpenData/2emc-na4n.tsv.gz', '2016-17 Physical Education - PE Instruction - School Level'
27, '/user/hm74/NYCOpenData/2enn-s52j.tsv.gz', 'Adult family health plus levels'

2. run the command: 
$ module load spark/2.4.0
$ module load python/gnu/3.6.5
$ spark-submit task1.py 0 1900
