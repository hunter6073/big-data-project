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
    if label == "lastname" or label =="firstname" or label =="middlename" or label == "fullname":
        return "Person name"
    if label == "coordinates":
        return "LAT/LON coordinates"
    if label == "boro":
        return "Borough"
    if label == "subject" or label == "study":
        return "Areas of study"
    if label == "level":
        return "School Levels"
    if label == "college" or label == "university":
        return "College/University names"
    if label == "building":
        return "Building Classification"
    if label == "type":
        return "Vehicle Type"
    if label == "location":
        return "Type of location"
    if label == "parks" or label =="playground":
        return "Parks/Playground"
    return label



main_directory = "./labelled_data/"
# get all files in the labelled_data folder
onlyfiles = [f for f in listdir(main_directory) if isfile(join(main_directory, f))]
for i in range(0,len(onlyfiles)):
    item = main_directory + onlyfiles[i] 
    print("this is the " + str(i)+" item out of "+str(len(onlyfiles))+" items")
    fileName = item # file name
    item = item.replace(".txt","").replace(main_directory,"").strip()
    vp = item.split("_",1)
    table = vp[0] # table name e.g. abjx-bcde
    column = vp[1] # column name e.g. SCHOOL_LEVEL

    ################################################
    # predict file label here
    # TODO: use more strategy to identify other labels
    predict_list = [] # could be multiple labels

    # strategy 1: identify using column name
    processed_name = column.replace("_","").replace(".","").replace("-","").strip().lower()
    for l in label_array:
        if l in processed_name:
            predict_list.append(link(l))
    # each table has its own predict_list, which is a list of predicted labels

    #################################################
    # get key_list, the actual labels of the column
    fp = open(fileName,"r")
    line = fp.readline()
    key_list = []
    while line:
        l_key = line.split(",")[0].replace("'","").strip()
        #TODO: l_key needs to be updated using the script in get_column_names
        if l_key == "Business Name":
            l_key = "Business name"
        if "name" in l_key:
            l_key = "Person name"
        if l_key == "Letter":
            l_key = "Other"
        if l_key == "Park":
            l_key = "Parks/Playgrounds"
        if l_key == "Phone number":
            l_key = "Phone Number"
        if l_key == "School levels":
            l_key = "School Levels"
        if l_key == "other":
            l_key = "Other"
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

for label in labels:
    # TODO: fix the script to get the true recall and precision

    predicted = 0 # all columns predicted as type
    correct = 0 # number of columns correctly predicted as type
    total = 0 # number of actual columns of type

    for item in data: # item[0] is the actuall list, item[1] is the predicted list
        if label in item[0]:
            total += 1
        if item[0] == item[1]:
            predicted += 1
        if label in item[0] and label in item[1]:
            correct += 1
    precision = float(float(correct)/float(predicted))
    recall = float(float(correct)/float(total))
    print("recall for label: "+ label +" is: " + str(recall))
    print("precision for label: "+ label +" is: "+str(precision))


# output results
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data)
#print(labels)

