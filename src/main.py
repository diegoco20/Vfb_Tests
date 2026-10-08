from src.connectome.loader import load_connectome
from src.brain.network import NeuralNetwork


def main():
    graph = load_connectome("data/test_connections.csv")
    network = NeuralNetwork(graph)

    print("VFB-Snake project initialized")
    print(f"Neurons: {graph.number_of_nodes()}")
    print(f"Connections: {graph.number_of_edges()}")

    print("\nSimulation:")

    for step in range(5):
        network.stimulate("neuron_A")

        activated = network.update()

        print(f"Step {step}: {activated}")


if __name__ == "__main__":
    main()