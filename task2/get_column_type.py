from os import listdir
from os.path import isfile, join
import pprint
data = {}
main_directory = "./labelled_data/"
# get all files in the labelled_data folder
onlyfiles = [f for f in listdir(main_directory) if isfile(join(main_directory, f))]
for i in range(0,len(onlyfiles)):
    item = main_directory + onlyfiles[i] 
    print("this is the " + str(i)+" item out of "+str(len(onlyfiles))+" items")
    fileName = item # file name
    item = item.replace(".txt","").strip()
    vp = item.split("_",1)
    table = vp[0] # table name
    column = vp[1] # column name

    # opening and reading file
    fp = open(fileName,"r")
    line = fp.readline()
    key_list = []
    while line:
        l_key = line.split(",")[0].replace("'","").strip()
        if l_key not in key_list:
            key_list.append(l_key) # add to the key_list array
        line = fp.readline()

    for kl_key in key_list: # add keys to data dictionary
        if kl_key in data.keys():
            data[kl_key] += 1
        else:
            data[kl_key] = 1
    fp.close()
# output results
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

