from random import seed
from data_prep import accuracy, column_means, column_stdevs, confusion_matrix, cross_validation_split, load_csv, normalize, standardize, str_column_to_float, train_test_split
seed(1)

actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]

m = confusion_matrix(actual, predicted)

print(m)

