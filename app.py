import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from graph_data import graph
from algorithm import dijkstra

st.title("DSS Wisata Kampung Adat Kawa")

nodes = list(graph.keys())

start = st.selectbox(
    "Pilih Lokasi Awal",
    nodes
)

goal = st.selectbox(
    "Pilih Tujuan",
    nodes
)

if st.button("Cari Rute"):

    cost, path = dijkstra(
        graph,
        start,
        goal
    )

    st.success(f"Total Jarak: {cost} km")

    st.write("Rute Terbaik:")
    st.write(" ➜ ".join(path))

G = nx.Graph()

for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

fig, ax = plt.subplots(figsize=(8, 6))

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    font_size=8,
    ax=ax
)

labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels,
    ax=ax
)

st.pyplot(fig)