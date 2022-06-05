from data_prep import load_csv, str_column_to_float, str_column_to_int

diabetes = 'pima-indians-diabetes.csv'
iris = 'iris.csv'


dataset = load_csv("./datasets/" + diabetes)

for c in range(len(dataset[0])):
	str_column_to_float(dataset, c)

print(dataset[0])


dataset = load_csv("./datasets/" + iris)


str_column_to_int(dataset, len(dataset[0]) - 1)
