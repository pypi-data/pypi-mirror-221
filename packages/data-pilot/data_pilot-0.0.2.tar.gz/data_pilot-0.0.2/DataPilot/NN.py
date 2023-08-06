import numpy as np

class SLP:

    def __init__(self, input_vector_size):
        self.weights = np.zeros(input_vector_size)
        self.bias = 0.0

    def __call__(self, input_vector):
        return self.predict(input_vector)

    def __str__(self):
        return f"SingleLayerPerceptron(weights={self.weights}, bias={self.bias})"

    def __repr__(self):
        return f"SingleLayerPerceptron(weights={self.weights}, bias={self.bias})"

    def __len__(self):
        return len(self.weights)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.weights[index]
        else:
            return self.weights[index]

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self.weights[index] = value
        else:
            self.weights[index] = value

    def __iter__(self):
        return iter(self.weights)

    def __next__(self):
        raise StopIteration

    def predict(self, input_vector):
        net_input = np.dot(self.weights, input_vector) + self.bias
        return self.activation(net_input)

    def activation(self, net_input):
        return 1 if net_input >= 0 else 0