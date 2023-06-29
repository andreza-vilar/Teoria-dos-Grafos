import networkx as nx
from src.Q01 import class_metrics


def silent_villains(ddc, threshold):
    if (ddc is None or threshold is None or threshold < 0):
        return None
    if not nx.is_directed(ddc):
        return None

    breakable = []
    butterfly = []
    hub = []

    for n in ddc.nodes():
        fan_out, fan_in = class_metrics(ddc, n)
        if fan_out > threshold:
            breakable.append(n)
        if fan_in > threshold:
            butterfly.append(n)
        if n in breakable and n in butterfly:
            hub.append(n)

    return breakable, butterfly, hub
