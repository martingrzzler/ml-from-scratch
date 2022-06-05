from csv import reader

def load_csv(filename):
	dataset = list()
	with open(filename, "r") as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)

	return dataset

def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()

	for i, value in enumerate(unique):
		lookup[value] = i

	for row in dataset:
		row[column] = lookup[row[column]]
	
	return lookup

def minmax(dataset):
	minmax = list()

	for c in range(len(dataset[0])):
		col_values = [row[c] for row in dataset]
		col_min = min(col_values)
		col_max = max(col_values)
		minmax.append([col_min, col_max])
	return minmax

def normalize(dataset):
	mm = minmax(dataset)
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - mm[i][0]) / (mm[i][1] - mm[i][0])