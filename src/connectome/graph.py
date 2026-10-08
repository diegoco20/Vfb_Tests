import networkx as nx


def create_test_graph():
    graph = nx.DiGraph()

    graph.add_edge("neuron_A", "neuron_B", weight=0.5)
    graph.add_edge("neuron_A", "neuron_C", weight=0.2)
    graph.add_edge("neuron_B", "neuron_C", weight=0.8)

    return graph