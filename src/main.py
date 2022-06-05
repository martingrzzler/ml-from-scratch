from data_prep import column_means, column_stdevs, load_csv, normalize, standardize, str_column_to_float

diabetes = 'pima-indians-diabetes.csv'
iris = 'iris.csv'


dataset = load_csv("./datasets/" + diabetes)

for c in range(len(dataset[0])):
	str_column_to_float(dataset, c)


print(dataset[0])

standardize(dataset)

print(dataset[0])
