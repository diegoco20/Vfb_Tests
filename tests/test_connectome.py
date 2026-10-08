from src.connectome.loader import load_connectome


def test_load_connectome():
    graph = load_connectome("data/test_connections.csv")

    assert graph.number_of_nodes() == 3
    assert graph.number_of_edges() == 3

    assert graph.has_edge("neuron_A", "neuron_B")
    assert graph.has_edge("neuron_A", "neuron_C")
    assert graph.has_edge("neuron_B", "neuron_C")