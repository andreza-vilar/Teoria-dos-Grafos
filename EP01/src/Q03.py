import networkx as nx
# Funções de apoio para testar o tipo de grafo
def has_multiple_edges(G): return (
    any(G.number_of_edges(e[0], e[1]) > 1 for e in G.edges))


def is_pseudograph(G): return nx.number_of_selfloops(G) > 0
def is_multigraph(G): return not is_pseudograph(G) and has_multiple_edges(G)
def is_simple(G): return not is_multigraph(G) and not is_pseudograph(G)


def graph_density(g):
    if (g is None):
        return None

    if (nx.is_empty(g)):
        return 0.00

    m = g.number_of_edges()
    n = g.number_of_nodes()

    if (nx.is_directed(g)):
        d = m/(n*(n-1))
        return round(d, 2)
    if (is_simple(g)):
        d = 2*m/(n*(n-1))
        return round(d, 2)
