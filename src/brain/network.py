from .neuron import Neuron


class NeuralNetwork:
    def __init__(self, graph):
        self.graph = graph

        self.neurons = {
            name: Neuron(name)
            for name in graph.nodes
        }

    def stimulate(self, neuron_name, value=1.0):
        self.neurons[neuron_name].receive(value)

    def update(self):
        activated = []

        for name, neuron in self.neurons.items():
            if neuron.update():
                activated.append(name)

        for name in activated:
            for target in self.graph.successors(name):
                self.neurons[target].receive(1.0)

        return activated