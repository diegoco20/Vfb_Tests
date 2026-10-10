class SnakeInterface:
    def __init__(self, network):
        self.network = network

    def stimulate_sensor(self, neuron_name, value=1.0):
        neuron = self.network.neurons[neuron_name]

        if neuron.neuron_type != "sensory":
            raise ValueError(
                f"{neuron_name} is not a sensory neuron"
            )

        self.network.stimulate(neuron_name, value)

    def get_motor_signals(self, activated):
        return [
            name
            for name in activated
            if self.network.neurons[name].neuron_type == "motor"
        ]