import csv

import networkx as nx


def load_connectome(path):
    graph = nx.DiGraph()

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            source = row["source"]
            target = row["target"]
            weight = float(row["weight"])

            graph.add_edge(
                source,
                target,
                weight=weight
            )

    return graph