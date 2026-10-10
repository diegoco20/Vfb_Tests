
from .neuron import Neuron


class NeuralNetwork:
    def __init__(self, graph):
        self.graph = graph

        self.neurons = {
            name: Neuron(
                name,
                neuron_type=graph.nodes[name].get(
                    "neuron_type",
                    "interneuron"
                )
            )
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
                weight = self.graph[name][target]["weight"]
                self.neurons[target].receive(weight)

        return activated