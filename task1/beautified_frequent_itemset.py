import os
import simplejson as json


directory_in_str = 'output'
directory = os.fsencode(directory_in_str)

TEXT 	= 'TEXT'
INTEGER = 'INTEGER (LONG)'
REAL 	= 'REAL'
DATE 	= 'DATE/TIME'

class Stat:
	def __init__(self, name):
		self.dataset 	= name
		self.textCount 	= 0
		self.textCols 	= []
		self.intCount 	= 0
		self.intCols 	= []
		self.dateCount 	= 0
		self.dateCols 	= []
		self.realCount 	= 0
		self.realCols 	= []
	def add(self, t, col):
		if t == TEXT:
			self.textCount += 1
			self.textCols.append(col)
		elif t == INTEGER:
			self.intCount += 1
			self.intCols.append(col)
		elif t == REAL:
			self.realCount += 1
			self.realCols.append(col)
		elif t == DATE:
			self.dateCount += 1
			self.dateCols.append(col)
	def get_stats(self):
		return {
			TEXT: 		self.textCount,
			INTEGER: 	self.intCount,
			REAL: 		self.dateCount,
			DATE: 		self.realCount
		}

	def get_2_itemset(self):
		result = {
			TEXT + ';' + INTEGER: 0,
			TEXT + ';' + REAL: 	0,
			TEXT + ';' + DATE: 	0,
			INTEGER + ';' + REAL: 0,
			INTEGER + ';' + DATE: 0,
			REAL + ';' + DATE: 	0
		}

		t = {col for col in self.textCols}
		i = {col for col in self.intCols}
		r = {col for col in self.realCols}
		d = {col for col in self.dateCols}
		
		for col in t:
			if col in i: result[TEXT + ';' + INTEGER] += 1
			if col in r: result[TEXT + ';' + REAL] += 1
			if col in d: result[TEXT + ';' + DATE] += 1

		for col in i:
			if col in r: result[INTEGER + ';' + REAL] += 1
			if col in d: result[INTEGER + ';' + DATE] += 1

		for col in r:
			if col in d: result[REAL + ';' + DATE] += 1

		return result

	def get_3_itemset(self):
		result = {
			TEXT + ';' + INTEGER + ';' + REAL: 	0,
			TEXT + ';' + REAL + ';' + DATE: 	0,
			TEXT + ';' + INTEGER  + ';' + DATE: 0,
			INTEGER + ';' + REAL + ';' + DATE: 	0
		}
		t = {col for col in self.textCols}
		i = {col for col in self.intCols}
		r = {col for col in self.realCols}
		d = {col for col in self.dateCols}

		for col in t:
			if col in i and col in r: result[TEXT + ';' + INTEGER + ';' + REAL] += 1
			if col in r and col in d: result[TEXT + ';' + REAL + ';' + DATE] += 1
			if col in i and col in d: result[TEXT + ';' + INTEGER  + ';' + DATE] += 1
		for col in i:
			if col in r and col in d: result[INTEGER + ';' + REAL + ';' + DATE] += 1

		return result

	def get_4_itemset(self):
		result = {
			TEXT + ';' + INTEGER + ';' + REAL + ';' + DATE: 	0,
		}
		t = {col for col in self.textCols}
		i = {col for col in self.intCols}
		r = {col for col in self.realCols}
		d = {col for col in self.dateCols}

		for col in t:
			if col in i and col in r and col in d: result[TEXT + ';' + INTEGER + ';' + REAL + ';' + DATE] += 1

		return result

class State:
	def __init__(self):
		self.datasets = []

	def add_dataset(self, dataset):
		self.datasets.append(dataset)

	def get_stats(self):
		stats = {
			TEXT: 		0,
			INTEGER: 	0,
			REAL: 		0,
			DATE: 		0
		}
		for dataset in self.datasets:
			stat = dataset.get_stats()
			stats[TEXT] += stat[TEXT]
			stats[INTEGER] += stat[INTEGER]
			stats[REAL] += stat[REAL]
			stats[DATE] += stat[DATE]

		return stats

	def get_2_itemset(self):
		stats = {
			TEXT + ';' + INTEGER: 0,
			TEXT + ';' + REAL: 	0,
			TEXT + ';' + DATE: 	0,
			INTEGER + ';' + REAL: 0,
			INTEGER + ';' + DATE: 0,
			REAL + ';' + DATE: 	0
		}

		for dataset in self.datasets:
			stat = dataset.get_2_itemset()
			stats[TEXT + ';' + INTEGER] += stat[TEXT + ';' + INTEGER]
			stats[TEXT + ';' + REAL] += stat[TEXT + ';' + REAL]
			stats[TEXT + ';' + DATE] += stat[TEXT + ';' + DATE]
			stats[INTEGER + ';' + REAL] += stat[INTEGER + ';' + REAL]
			stats[INTEGER + ';' + DATE] += stat[INTEGER + ';' + DATE]
			stats[REAL + ';' + DATE] += stat[REAL + ';' + DATE]

		return stats

	def get_3_itemset(self):
		stats = {
			TEXT + ';' + INTEGER + ';' + REAL: 	0,
			TEXT + ';' + REAL + ';' + DATE: 	0,
			TEXT + ';' + INTEGER  + ';' + DATE: 0,
			INTEGER + ';' + REAL + ';' + DATE: 	0
		}

		for dataset in self.datasets:
			stat = dataset.get_3_itemset()
			stats[TEXT + ';' + INTEGER + ';' + REAL] += stat[TEXT + ';' + INTEGER + ';' + REAL]
			stats[TEXT + ';' + REAL + ';' + DATE] += stat[TEXT + ';' + REAL + ';' + DATE]
			stats[TEXT + ';' + INTEGER  + ';' + DATE] += stat[TEXT + ';' + INTEGER  + ';' + DATE]
			stats[INTEGER + ';' + REAL + ';' + DATE] += stat[INTEGER + ';' + REAL + ';' + DATE]

		return stats

	def get_4_itemset(self):
		stats = {
			TEXT + ';' + INTEGER + ';' + REAL + ';' + DATE: 0
		}
		for dataset in self.datasets:
			stat = dataset.get_4_itemset()
			stats[TEXT + ';' + INTEGER + ';' + REAL + ';' + DATE] += stat[TEXT + ';' + INTEGER + ';' + REAL + ';' + DATE]

		return stats

datasets = []



state = State()

none_col = 0
none_being_most = 0
total_col = 0
number_column_types = [0, 0, 0, 0]
column_name_length = {}
times = []
longest_file = ''
longest_elapsed = 0
key_column_candidates_count = 0


max_int = 0
min_int = 10000000
max_date = None
min_date = None
dates = []
max_real = 0
min_real = 10000000
longest_5_string = []
int_mean = []
real_mean = []
int_std = []
real_std = []
avg_length = []

print('start beautifing')
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".json"):
		with open('output/' + filename) as f:
			obj = json.load(f)

			timing = int(obj['time_elapsed'])
			if timing > longest_elapsed:
				longest_elapsed = timing
				longest_file = filename
			times.append(timing)
			# for each type, how many columns contain that type
			dataset = Stat(filename.split('.')[0])

			for col in obj['columns']:
				if len(obj['columns'][col]['column_name']) not in column_name_length:
					column_name_length[len(obj['columns'][col]['column_name'])] = [1, [obj['columns'][col]['column_name']]]
				else:
					column_name_length[len(obj['columns'][col]['column_name'])][0] += 1
					column_name_length[len(obj['columns'][col]['column_name'])][1].append(obj['columns'][col]['column_name'])
				for t in obj['columns'][col]['data_types']:
					dataset.add(t['type'], col)

					if t['type'] == INTEGER:
						if t['max_value'] > max_int: max_int = t['max_value']
						if t['min_value'] < min_int: min_int = t['min_value']
						int_mean.append(t['mean'])
						int_std.append(t['stddev'])
					elif t['type'] == REAL:
						if t['max_value'] > max_real: max_real = t['max_value']
						if t['min_value'] < min_real: min_real = t['min_value']
						real_mean.append(t['mean'])
						real_std.append(t['stddev'])
					elif t['type'] == DATE:
						dates.append(t['max_value'])
						dates.append(t['min_value'])
					elif t['type'] == TEXT:
						longest_5_string += t['longest_values']
						longest_5_string.sort(reverse=True, key=lambda x: len(x))
						longest_5_string = longest_5_string[:5]
						avg_length.append(t['average_length'])

				number_column_types[len(obj['columns'][col]['data_types']) - 1] += 1
				if None in obj['columns'][col]['frequent_values']:
					if obj['columns'][col]['frequent_values'][0] == None:
						none_being_most += 1
					none_col += 1
				total_col += 1

			if len(obj['key_column_candidates']) != 0:
				key_column_candidates_count += 1
			state.add_dataset(dataset)
			resulting_list = []
			for col in obj['columns']:
				resulting_list.append(obj['columns'][col])

			obj['columns'] = resulting_list
			outfile = open('Beautified_Output/'+filename, "w")
			outfile.write(json.dumps(obj, indent=4))
			outfile.close()

print('finish beautified')

print('calculating frequent itemsets...')
print('frequent 1 itemsets')
print(state.get_stats())
print('frequent 2 itemsets')
print(state.get_2_itemset())
print('frequent 3 itemsets')
print(state.get_3_itemset())
print('frequent 4 itemsets')
print(state.get_4_itemset())

print("# cols being most frequent value:", none_being_most)
print("# cols has None as frequent value:",none_col)
print("total # cols:", total_col)
print("number of columns per number of data types that one column has\n", number_column_types)

times.sort()
starting_time = times[0]
window = 50
count = 0
d = {}

for i in range(len(times)):
	curr_time = times[i]
	if curr_time - starting_time <= window:
		count += 1
	else:
		d[starting_time] = count
		starting_time = curr_time
		count = 1

print(d)

count_min = [0] * (30)
count_hour = [0] * 10
i = 0

for m in range(len(count_min)):
	start_min = m * 60
	end_min = m * 60 + 60
	while i < len(times):
		if start_min <= times[i] <= end_min:
			count_min[m] += 1
			i += 1
		else:
			break

for h in range(len(count_hour)):
	start_hour = h * 60 * 60
	end_hour = (h + 1) * 60 * 60

	while i < len(times):
		if start_hour <= times[i] <= end_hour:
			count_hour[h] += 1
			i += 1
		else:
			break

print(count_min)
print(count_hour)
print(longest_elapsed, filename)
print("key column candidate count", key_column_candidates_count)

max_length = max([key for key in column_name_length])
print(max_length, column_name_length[max_length])

print("global max int:", max_int)
print("global min int:", min_int)
print("global max real:", max_real)
print("global min real:", min_real)
print("ints mean")
print(len([int(i) for i in int_mean if int(i) == 0]))
print('ints std')
# print(int_std)

print("reals mean")
# print(real_mean)
print('real std')
# print(real_std)

# print(dates)
# print([int(i) for i in avg_length])
print([len(i) for i in longest_5_string])