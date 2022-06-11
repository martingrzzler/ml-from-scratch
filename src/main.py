from random import seed
from model.baseline import ZeroRuleModel, Type
seed(1)

train = [[10], [15], [12], [15], [18], [20]]
test = [[None], [None], [None], [None]]


model = ZeroRuleModel()
model.fit(train)
print(model.predict(test, Type.REGRESSION))

