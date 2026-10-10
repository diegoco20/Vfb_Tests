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
    
def test_neuron_type():
    neuron = Neuron("vision_left", neuron_type="sensory")

    assert neuron.neuron_type == "sensory"


def test_invalid_neuron_type():
    import pytest

    with pytest.raises(ValueError):
        Neuron("unknown", neuron_type="invalid")