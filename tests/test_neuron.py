from src.brain.neuron import Neuron


def test_neuron_below_threshold():
    neuron = Neuron("test")

    neuron.receive(0.5)

    assert neuron.update() is False


def test_neuron_reaches_threshold():
    neuron = Neuron("test")

    neuron.receive(1.0)

    assert neuron.update() is True