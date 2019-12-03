
filenames = []
labels = ['Other',
          'School name',
          'Subjects in school',
          'School name',
          'School Levels',
          'Person name - First name',
          'Person name - First name',
          'Person name - Last name',
          'Zip code',
          'Street name',
          'Zip code',
          'Other',
          'City agency',
          'Other',
          'Other',
          'Street name',
          'Parks/Playgrounds',
          'Subjects in school',
          'Vehicle Type',
          'Color',
          'LAT/LON coordinates',
          'City',
          'Zip code',
          'School Levels',
          'Websites',
          'Address',
          'Phone Number',
          'Phone Number',
          'School Levels',
          'Subjects in school',
          'Address',
          'LAT/LON coordinates',
          'Vehicle Type',
          'Vehicle Type',
          'Vehicle Type',
          'Vehicle Type',
          'Vehicle Type',
          'Street name',
          'School name',
          'Street name',
          'Street name',
          'Subjects in school',
          'Person name - First name',
          'Person name - First name',
          'Person name - Last name',
          'LAT/LON coordinates',
          'City agency',
          'Address',
          'Color',
          'Car make',
          'City',
          'Other',
          'Borough',
          'Street name',
          'Vehicle Type',
          'Color',
          'Car make',
          'Websites',
          'Street name',
          'Other',
          'LAT/LON coordinates',
          'Subjects in school',
          'City agency',
          'City agency',
          'Person name - First name',
          'Person name - Last name',
          'Person name - Other',
          'School Levels',
          'Color',
          'LAT/LON coordinates',
          'Neighborhood',
          'City',
          'Zip code',
          'Car make',
          'City',
          'Phone Number',
          'Address',
          'Other',
          'Street name',
          'School name',
          'School name',
          'Address',
          'Subjects in school',
          'Car make',
          'Address',
          'Zip code',
          'Vehicle Type',
          'Color']


import simplejson as json


f = open("files.txt", 'r')

for line in f:
    line = line.strip()
    filenames.append(line)

f.close()

counter = 0
while counter < len(filenames):
    fileName = filenames[counter]
    label = labels[counter]
    counter += 1
    f1 = open('Done/' + fileName + "/part-00000","r")
    f2 = open('Done/' + fileName + "/part-00001","r")
    line = f1.readline()
    line = f1.readline()
    item_arr = []
    while line:
        value = str(line.strip().split(",")[len(line.split(","))-1])
        key = line.replace(","+value,"").strip()
        key = "'"+key+"'"
        result = "'"+label+"', "+key+", "+value
        item_arr.append(result)
        line = f1.readline()

    line = f2.readline()
    while line:
        value = str(line.strip().split(",")[len(line.split(","))-1])
        key = line.replace(value,"").strip()
        key = "'"+key+"'"
        result = "'"+label+"', "+key+", "+value
        item_arr.append(result)
        line = f2.readline()

    f1.close()
    f2.close()
    output_file = "./output/"+fileName.replace(".out",".txt")
    print(output_file)
    out = open(output_file,"w+")
    for item in item_arr:
        out.write(item)
        out.write("\n")
    out.close()

