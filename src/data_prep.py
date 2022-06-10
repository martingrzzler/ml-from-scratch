from cmath import sqrt
from csv import reader
from random import randrange
from statistics import variance

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


def column_means(dataset):
	means = [0] * len(dataset[0])
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i] = sum(col_values) / float(len(dataset))
	return means

def column_stdevs(dataset):
	stdevs = [0] * len(dataset[0])
	means = column_means(dataset)
	for i in range(len(dataset[0])):
		squared_diff = [pow(row[i] - means[i], 2) for row in dataset]
		stdevs[i] = sum(squared_diff)
	stdevs = [(x/(float(len(dataset) - 1))) ** 0.5 for x in stdevs]
	return stdevs
		

def standardize(dataset):
	means = column_means(dataset)
	stdevs = column_stdevs(dataset)

	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - means[i]) / stdevs[i]
	
def train_test_split(dataset, split=0.6):
	train = list()
	train_size = len(dataset) * split
	# list() creates copy
	test = list(dataset)

	while len(train) < train_size:
		index = randrange(len(test))
		train.append(test.pop(index))

	return train, test


