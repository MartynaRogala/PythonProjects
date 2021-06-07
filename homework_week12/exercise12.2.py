import networkx as nx

G = nx.Graph()
for node in (1, 2, 3, 4, 5, 6, 7, 8, 9):
    G.add_node(node)
for (a, b) in [(1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (5, 1), (1, 6), (5, 6), (5, 7), (6, 7), (3, 5), (2, 6), (5, 8),
               (3, 8), (2, 9), (6, 9)]:
    G.add_edge(a, b)

import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, font_weight='bold', node_size=300, node_color='green', edge_color="red",
        font_color="white")
plt.show()
