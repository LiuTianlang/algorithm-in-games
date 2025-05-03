"""
Railway Construction on Mars – MST-Based Optimization Inspired by Surviving Mars

This script simulates the construction of an optimal railway network between bases
on Mars, inspired by the game *Surviving Mars*. Each base is represented as a node,
and potential railway connections between bases have randomly assigned costs.

We apply **Prim's Algorithm** to build a **Minimum Spanning Tree (MST)** — a network
that connects all bases with the minimal total railway construction cost, ensuring
no cycles and full connectivity.

Features:
- Randomly generates a weighted undirected graph representing base connections
- Applies Prim's algorithm using a priority queue (min-heap)
- Visualizes the full graph and highlights the MST using NetworkX

This simulation can serve as a base model for designing infrastructure planning tools
in games or real-world logistics problems involving cost-efficient network design.
"""
import networkx as nx
import random
import heapq
import matplotlib.pyplot as plt

# Generate a fully connected undirected weighted graph
def generate_graph(num_nodes):
    start_end_weights = {}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10)
            # Add both directions since the graph is undirected
            if random.random() < 0.5:
                start_end_weights[(i, j)] = weight
                start_end_weights[(j, i)] = weight
    return start_end_weights

# Prim's algorithm to build a minimum spanning tree
def prim(num_nodes, start_end_weights):
    # Initialize visited nodes set and heap with edges from node 0
    visited_nodes = set()
    visited_nodes.add(0)

    weight_heap = []
    min_node_weights = {}

    for (u, v), weight in start_end_weights.items():
        if u == 0:
            heapq.heappush(weight_heap, (weight, (u, v)))

    # Keep adding the lowest-cost edge until all nodes are visited
    while len(visited_nodes) < num_nodes:
        while weight_heap:
            min_weight, (u, v) = heapq.heappop(weight_heap)
            # Only consider edges leading to unvisited nodes
            if v not in visited_nodes:
                break
        else:
            # If no more usable edges and some nodes are unvisited, the graph is disconnected
            raise ValueError("Graph is not connected.")

        # Add the new node and the edge to the MST
        visited_nodes.add(v)
        min_node_weights[(u, v)] = min_weight

        # Push all edges from the new node into the heap
        for (a, b), weight in start_end_weights.items():
            if a == v and b not in visited_nodes:
                heapq.heappush(weight_heap, (weight, (a, b)))

    # Print the MST result
    print("Prim's algorithm:")
    for (u, v), weight in min_node_weights.items():
        print(f"Edge ({u}, {v}) with weight {weight}")

    return min_node_weights

# Draw the full graph and highlight the minimum spanning tree edges
def draw_graph(start_end_weights, min_node_weights):
    G = nx.Graph()

    # Add all edges to the graph
    for (start, end), weight in start_end_weights.items():
        G.add_edge(start, end, weight=weight)

    # Extract the MST edge list
    mst_edges = list(min_node_weights.keys())

    # Layout for visualization
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))

    # Draw all edges in gray
    nx.draw_networkx_edges(G, pos, edge_color='black', alpha=0.5)

    # Draw MST edges in green
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=2)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    # Draw edge weights as labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Graph with Minimum Spanning Tree")
    plt.legend([ 'Other Edges','MST Edges'], loc='upper left')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))  

    if num_nodes > 2:
        start_end_weights = generate_graph(num_nodes)

        print("Generated graph with weights:")
        for (u, v), weight in start_end_weights.items():
            if u < v:  # avoid printing both directions
                print(f"Edge ({u}, {v}) has weight {weight}")

        min_node_weights = prim(num_nodes, start_end_weights)
        draw_graph(start_end_weights, min_node_weights)
