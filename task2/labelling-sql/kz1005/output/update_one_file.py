f = open('itd7-gx3g_Location_1.txt', 'r')

l = []
for line in f:
	line = line.replace("'City agency'", "'LAT/LON coordinates'")
	l.append(line)

wf = open('itd7-gx3g_Location_1_copy.txt', 'w')
for one in l:
	wf.write(one)


f.close()
wf.close()