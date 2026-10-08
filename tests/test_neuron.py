from src.brain.neuron import Neuron


def test_neuron_below_threshold():
    neuron = Neuron("test")

    neuron.receive(0.5)

    assert neuron.update() is False


def test_neuron_reaches_threshold():
    neuron = Neuron("test")

    neuron.receive(1.0)

    assert neuron.update() is True


def test_neuron_accumulates_over_time():
    neuron = Neuron("test")

    neuron.receive(0.4)
    assert neuron.update() is False

    neuron.receive(0.4)
    assert neuron.update() is False

    neuron.receive(0.3)
    assert neuron.update() is True