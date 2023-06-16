from typing import List, Dict
import networkx as nx

def best_route(G: nx.Graph, start_node: int) -> List[int]:
    if G is None or start_node not in G.nodes:
        return None

    for node in G.nodes():
        if 'depth' not in G.nodes[node]:
            G.nodes[node]['depth'] = 0
        if 'full' not in G.nodes[node]:
            G.nodes[node]['full'] = False

    current_depth = G.nodes[start_node]['depth']
    visited_nodes = [start_node]

    while True:
        comp_data = [(n, G.nodes[n]['full']) for n in G.nodes()]
        next_comp_idx = find_next_empty_component(comp_data, visited_nodes[-1])

        if next_comp_idx == -1:
            return visited_nodes

        neighbors = list(G.neighbors(visited_nodes[-1]))

        candidates = [n for n in neighbors if G.nodes[n]['depth'] > current_depth and not G.nodes[n]['full']]

        if not candidates:
            return visited_nodes

        next_node = min(candidates, key=lambda x: G.nodes[x]['depth'])
        visited_nodes.append(next_node)

        G.nodes[next_node]['full'] = True
        current_depth = G.nodes[next_node]['depth']


def find_next_empty_component(components: List[Dict[int, bool]], start_idx: int) -> int:
    
    for idx, comp in enumerate(components[start_idx:], start=start_idx):
        if not comp[1]:
            return idx

    return -1
