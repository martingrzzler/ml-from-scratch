from random import seed
from data_prep import RandomModel, Type, ZeroRuleModel, confusion_matrix, mean_absolute_error, print_confusion_matrix, root_mean_squared_error 
seed(1)

train = [[10], [15], [12], [15], [18], [20]]
test = [[None], [None], [None], [None]]


model = ZeroRuleModel()
model.fit(train)
print(model.predict(test, Type.REGRESSION))

