import networkx as nx


def class_metrics(ddc, c):
    if (ddc is None or c is None):
        return None
    if (c not in ddc.nodes()):
        return None
    if not nx.is_directed(ddc):
        return None

    fan_out = len(list(ddc.successors(c)))
    fan_in = len(list(ddc.predecessors(c)))

    return fan_out, fan_in
