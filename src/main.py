from data_prep import load_csv, normalize, str_column_to_float, str_column_to_int

diabetes = 'pima-indians-diabetes.csv'
iris = 'iris.csv'


dataset = load_csv("./datasets/" + diabetes)

for c in range(len(dataset[0])):
	str_column_to_float(dataset, c)

normalize(dataset)

print(dataset[0])




