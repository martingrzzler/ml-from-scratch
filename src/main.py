from random import seed
from data_prep import column_means, column_stdevs, load_csv, normalize, standardize, str_column_to_float, train_test_split


dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

seed(1)
train, test = train_test_split(dataset)

print(train)
print(test)