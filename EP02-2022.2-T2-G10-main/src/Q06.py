import networkx as nx
from src.Q04 import mfs_greedy


def class_order(ddc):

    if ddc is None or not isinstance(ddc, nx.DiGraph):
        return None

    def topological_sort(graph):
        return list(reversed(list(nx.topological_sort(graph))))

    def get_subgraph_without_mfs(graph, mfs):
        subgraph = graph.copy()
        subgraph.remove_edges_from(mfs)
        return subgraph

    # Calcula o MFS do DDC
    mfs = mfs_greedy(ddc)

    # Obtém o subgrafo acíclico excluindo as arestas do MFS
    subgraph = get_subgraph_without_mfs(ddc, mfs)

    # Obtém a ordem topológica inversa do subgrafo acíclico
    order = topological_sort(subgraph)

    # Agrupa as classes que podem ser integradas ao mesmo tempo
    integration_order = []
    group = []
    for node in order:
        if node not in ddc.nodes:
            continue
        predecessors = list(ddc.predecessors(node))
        if all(p in integration_order for p in predecessors):
            group.append(node)
        else:
            if group:
                integration_order.append(group)
                group = [node]
            else:
                group.append(node)

    if group:
        integration_order.append(group)

    return integration_order

