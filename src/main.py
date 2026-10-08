from connectome.loader import load_connectome
from brain.network import NeuralNetwork


def main():
    graph = load_connectome("data/test_connections.csv")
    network = NeuralNetwork(graph)

    print("VFB-Snake project initialized")
    print(f"Neurons: {graph.number_of_nodes()}")
    print(f"Connections: {graph.number_of_edges()}")

    network.stimulate("neuron_A")

    print("\nSimulation:")

    for step in range(3):
        activated = network.update()
        print(f"Step {step}: {activated}")


if __name__ == "__main__":
    main()