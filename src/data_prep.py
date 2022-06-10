from cmath import sqrt
from csv import reader
import enum
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

def cross_validation_split(dataset, folds=3):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / folds)

	for i in range(folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

def accuracy(actual, predicted):
	correct = 0 
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct+=1
	return correct / float(len(actual)) * 100.0

def confusion_matrix(actual, predicted):
	classes = set(actual)
	matrix = [list([0] * len(classes)) for x in range(len(classes))]
	lookup = dict()
	for i, value in enumerate(classes):
		lookup[value] = i
	for i in range(len(actual)):
		x = lookup[actual[i]]
		y = lookup[predicted[i]]
		matrix[y][x]+=1
	return classes, matrix

def print_confusion_matrix(M, classes):
	print(' A ' + ' '.join(str(x) for x in classes))
	print('P---')
	for i, x in enumerate(classes):
		print("%s| %s" % (x, ' '.join(str(x) for x in M[i])))

def mean_absolute_error(actual, predicted):
	sum_error = 0
	for i in range(len(actual)):
		sum_error += abs(predicted[i] - actual[i])
	return sum_error / len(actual)

def root_mean_squared_error(actual, predicted):
	sum_error = 0
	for i in range(len(actual)):
		sum_error += (predicted[i] - actual[i]) ** 2
	return (sum_error / len(actual))**0.5



