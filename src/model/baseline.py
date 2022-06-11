from random import randrange
import enum

class RandomModel():
	def __init__(self) -> None:
		self.unique_outputs = None
		pass

	def fit(self, train):
		output_values = [row[-1] for row in train]
		self.unique_outputs = list(set(output_values))

	def predict(self, X):
		predictions = list()
		for row in X:
			index = randrange(len(self.unique_outputs))
			predictions.append(self.unique_outputs[index])
		return predictions

class Type(enum.Enum):
	CLASSIFICATION = 0
	REGRESSION = 1



class ZeroRuleModel:
	def __init__(self) -> None:
		self.output_values = None
		
	def fit(self, train):
		self.output_values = [row[-1] for row in train]

	def __get_prediction(self, type):
			if type == Type.CLASSIFICATION:
				return max(set(self.output_values), key=self.output_values.count)
			elif type == Type.REGRESSION:
				return sum(self.output_values) / len(self.output_values)
			else:
				raise Exception("unsupported type")

	def predict(self, X, type=Type.CLASSIFICATION):
		prediction = self.__get_prediction(type)
		return [prediction] * len(X)
		