from src.brain.network import NeuralNetwork
from src.connectome.loader import load_connectome


def test_network_stimulates_neuron():
    graph = load_connectome("data/test_connections.csv")
    network = NeuralNetwork(graph)

    network.stimulate("neuron_A")

    activated = network.update()

    assert activated == ["neuron_A"]


def test_network_propagates_weight():
    graph = load_connectome("data/test_connections.csv")
    network = NeuralNetwork(graph)

    network.stimulate("neuron_A")

    network.update()

    assert network.neurons["neuron_B"].input_value == 0.5
    assert network.neurons["neuron_C"].input_value == 0.2