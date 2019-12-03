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
			TEXT + INTEGER: 0,
			TEXT + REAL: 	0,
			TEXT + DATE: 	0,
			INTEGER + REAL: 0,
			INTEGER + DATE: 0,
			REAL + DATE: 	0
		}

		t = {col for col in self.textCols}
		i = {col for col in self.intCols}
		r = {col for col in self.realCols}
		d = {col for col in self.dateCols}
		
		for col in t:
			if col in i: result[TEXT + INTEGER] += 1
			if col in r: result[TEXT + REAL] += 1
			if col in d: result[TEXT + DATE] += 1

		for col in i:
			if col in r: result[INTEGER + REAL] += 1
			if col in d: result[INTEGER + DATE] += 1

		for col in r:
			if col in d: result[REAL + DATE] += 1

		return result

	def get_3_itemset(self):
		result = {
			TEXT + INTEGER + REAL: 	0,
			TEXT + REAL + DATE: 	0,
			TEXT + INTEGER  + DATE: 0,
			INTEGER + REAL + DATE: 	0
		}
		t = {col for col in self.textCols}
		i = {col for col in self.intCols}
		r = {col for col in self.realCols}
		d = {col for col in self.dateCols}

		for col in t:
			if col in i and col in r: result[TEXT + INTEGER + REAL] += 1
			if col in r and col in d: result[TEXT + REAL + DATE] += 1
			if col in i and col in d: result[TEXT + INTEGER  + DATE] += 1
		for col in i:
			if col in r and col in d: result[INTEGER + REAL + DATE] += 1

		return result

	def get_4_itemset(self):
		result = {
			TEXT + INTEGER + REAL + DATE: 	0,
		}
		t = {col for col in self.textCols}
		i = {col for col in self.intCols}
		r = {col for col in self.realCols}
		d = {col for col in self.dateCols}

		for col in t:
			if col in i and col in r and col in d: result[TEXT + INTEGER + REAL + DATE] += 1

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
			TEXT + INTEGER: 0,
			TEXT + REAL: 	0,
			TEXT + DATE: 	0,
			INTEGER + REAL: 0,
			INTEGER + DATE: 0,
			REAL + DATE: 	0
		}

		for dataset in self.datasets:
			stat = dataset.get_2_itemset()
			stats[TEXT + INTEGER] += stat[TEXT + INTEGER]
			stats[TEXT + REAL] += stat[TEXT + REAL]
			stats[TEXT + DATE] += stat[TEXT + DATE]
			stats[INTEGER + REAL] += stat[INTEGER + REAL]
			stats[INTEGER + DATE] += stat[INTEGER + DATE]
			stats[REAL + DATE] += stat[REAL + DATE]

		return stats

	def get_3_itemset(self):
		stats = {
			TEXT + INTEGER + REAL: 	0,
			TEXT + REAL + DATE: 	0,
			TEXT + INTEGER  + DATE: 0,
			INTEGER + REAL + DATE: 	0
		}

		for dataset in self.datasets:
			stat = dataset.get_3_itemset()
			stats[TEXT + INTEGER + REAL] += stat[TEXT + INTEGER + REAL]
			stats[TEXT + REAL + DATE] += stat[TEXT + REAL + DATE]
			stats[TEXT + INTEGER  + DATE] += stat[TEXT + INTEGER  + DATE]
			stats[INTEGER + REAL + DATE] += stat[INTEGER + REAL + DATE]

		return stats

	def get_4_itemset(self):
		stats = {
			TEXT + INTEGER + REAL + DATE: 0
		}
		for dataset in self.datasets:
			stat = dataset.get_4_itemset()
			stats[TEXT + INTEGER + REAL + DATE] += stat[TEXT + INTEGER + REAL + DATE]

		return stats

datasets = []



state = State()

print('start beautifing')
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".json"):
		with open('output/' + filename) as f:
			obj = json.load(f)

			# for each type, how many columns contain that type
			dataset = Stat(filename.split('.')[0])
			for col in obj['columns']:
				for t in obj['columns'][col]['data_types']:
					dataset.add(t['type'], col)
			state.add_dataset(dataset)

			outfile = open('Beautified_Output/beautified_' + filename, "w")
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
# 

