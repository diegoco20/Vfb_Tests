import networkx as nx


def create_test_graph():
    graph = nx.DiGraph()

    graph.add_edge("neuron_A", "neuron_B")
    graph.add_edge("neuron_B", "neuron_C")
    graph.add_edge("neuron_A", "neuron_C")

    return graph