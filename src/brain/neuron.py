class Neuron:
    def __init__(self, name, threshold=1.0, leak=0.0):
        self.name = name
        self.threshold = threshold
        self.leak = leak

        self.membrane_potential = 0.0
        self.input_value = 0.0
        self.active = False

    def receive(self, value):
        self.input_value += value

    def update(self):
        # Integrate input
        self.membrane_potential += self.input_value

        # Reset input for the next time step
        self.input_value = 0.0

        # Apply membrane leak
        self.membrane_potential -= self.leak

        # Prevent negative membrane potential
        self.membrane_potential = max(
            0.0,
            self.membrane_potential
        )

        # Check threshold
        if self.membrane_potential >= self.threshold:
            self.active = True

            # Reset after spike
            self.membrane_potential = 0.0

        else:
            self.active = False

        return self.active