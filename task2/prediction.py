from os import listdir
from os.path import isfile, join
import pprint
data = []
labels = []

label_array = ["lastname","firstname","middlename","fullname",
                   "businessname","phone","address","streetname",
                   "city","neighborhood","coordinates","zip","boro",
                   "schoolname","color","make","agency","study","subject",
                   "level","college","university","website","building","type","location",
                   "parks","playground"
                  ]
                  
def link(label):

    if label == "coordinates":
        return "lat/lon coordinates"
    if label == "boro":
        return "borough"
    if label == "subject" or label == "study":
        return "areas of study"
    if label == "level":
        return "school level"
    if label == "college" or label == "university":
        return "college/university names"
    if label == "building":
        return "building classification"
    if label == "type":
        return "vehicle type"
    if label == "location":
        return "type of location"
    if label == "parks" or label =="playground":
        return "parks/playground"
    return label

# def strategy_column_name():
# def strategy_column_name_with_words():
# def strategy_machine_learning():
# def strategy_mix

main_directory = "./labelled_data/"
# get all files in the labelled_data folder
onlyfiles = [f for f in listdir(main_directory) if isfile(join(main_directory, f))]
for i in range(0,len(onlyfiles)):
    item = main_directory + onlyfiles[i] 
    print("this is the " + str(i)+" item out of "+str(len(onlyfiles))+" items")
    fileName = item # file name
    item = item.replace(".txt","").replace(main_directory,"").strip()
    vp = item.split("_",1)
    table = vp[0] # table name
    column = vp[1] # column name

    ################################################
    # predict file label here
    predict_list = [] # could be multiple labels

    # strategy 1: identify using column name
    processed_name = column.replace("_","").replace(".","").replace("-","").strip().lower()
    #print(processed_name)

    for l in label_array:
        if l in processed_name:
            predict_list.append(link(l))


    #################################################
    # get key_list, the actual labels of the column
    fp = open(fileName,"r")
    line = fp.readline()
    key_list = []
    while line:
        l_key = line.split(",")[0].replace("'","").strip()
        if l_key not in key_list:
            key_list.append(l_key) # add to the key_list array
        if l_key not in labels:
            labels.append(l_key)
        line = fp.readline()
    fp.close()
    
    # key_list contains the actual labels of this table
    # predict_list contains the predicted labels of this table
    data.append((key_list,predict_list))
    ################################################


correct = 0
total = len(data)
for item in data:
    if item[0] == item[1]:
        correct += 1
print("precision is: " + str(float(correct/total)))

for label in labels:
    correct = 0
    total = 0
    for item in data:
        if label in item[0]:
            total += 1
        if item[0] == item[1]:
            correct += 1
    print("recall for label: "+ label +" is: " + str(float(correct/total)))
    print("precision for label: "+ label +" is: not ye calculated")


# output results
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data)
#print(labels)

