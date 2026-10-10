
class Neuron:
    def __init__(
        self,
        name,
        threshold=1.0,
        leak=0.0,
        neuron_type="interneuron"
    ):
        valid_types = {"sensory", "interneuron", "motor"}

        if neuron_type not in valid_types:
            raise ValueError(
                f"Invalid neuron type: {neuron_type}"
            )

        self.name = name
        self.neuron_type = neuron_type
        self.threshold = threshold
        self.leak = leak

        self.membrane_potential = 0.0
        self.input_value = 0.0
        self.active = False

    def receive(self, value):
        self.input_value += value

    def update(self):
        self.membrane_potential += self.input_value
        self.input_value = 0.0

        self.membrane_potential -= self.leak
        self.membrane_potential = max(
            0.0,
            self.membrane_potential
        )

        if self.membrane_potential >= self.threshold:
            self.active = True
            self.membrane_potential = 0.0
        else:
            self.active = False

        return self.active