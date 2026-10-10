from src.brain.network import NeuralNetwork
from src.connectome.loader import load_connectome
from src.brain.interface import SnakeInterface


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
    
def test_network_reads_neuron_types():
    graph = load_connectome("data/test_connections.csv")

    graph.nodes["neuron_A"]["neuron_type"] = "sensory"
    graph.nodes["neuron_C"]["neuron_type"] = "motor"

    network = NeuralNetwork(graph)

    assert network.neurons["neuron_A"].neuron_type == "sensory"
    assert network.neurons["neuron_B"].neuron_type == "interneuron"
    assert network.neurons["neuron_C"].neuron_type == "motor"
    
def test_interface_stimulates_sensory_neuron():
    graph = load_connectome("data/test_connections.csv")
    graph.nodes["neuron_A"]["neuron_type"] = "sensory"

    network = NeuralNetwork(graph)
    interface = SnakeInterface(network)

    interface.stimulate_sensor("neuron_A", 0.7)

    assert network.neurons["neuron_A"].input_value == 0.7


def test_interface_rejects_non_sensory_neuron():
    import pytest

    graph = load_connectome("data/test_connections.csv")
    network = NeuralNetwork(graph)
    interface = SnakeInterface(network)

    with pytest.raises(ValueError):
        interface.stimulate_sensor("neuron_A")


def test_interface_returns_only_motor_signals():
    graph = load_connectome("data/test_connections.csv")
    graph.nodes["neuron_C"]["neuron_type"] = "motor"

    network = NeuralNetwork(graph)
    interface = SnakeInterface(network)

    signals = interface.get_motor_signals(
        ["neuron_A", "neuron_C"]
    )

    assert signals == ["neuron_C"]