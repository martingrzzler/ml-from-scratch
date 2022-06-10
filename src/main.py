from random import seed
from data_prep import confusion_matrix, mean_absolute_error, print_confusion_matrix, root_mean_squared_error 
seed(1)

actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]
mae = root_mean_squared_error(actual, predicted)
print(mae)


