class Neuron:
    def __init__(self, name, threshold=1.0):
        self.name = name
        self.threshold = threshold
        self.input_value = 0.0
        self.active = False

    def receive(self, value):
        self.input_value += value

    def update(self):
        self.active = self.input_value >= self.threshold
        self.input_value = 0.0

        return self.active