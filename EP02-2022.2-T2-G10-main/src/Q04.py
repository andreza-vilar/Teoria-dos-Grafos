import networkx as nx
from src.Q01 import class_metrics
 
# Encontra os ciclos de dependência mínima em um grafo direcionado.
# Args: ddc (networkx.DiGraph): Grafo direcionado.
# Returns: list: Lista de ciclos, onde cada ciclo é representado como uma lista de arcos.
def find_minimum_dependency_cycles(ddc):
    cycle_nodes = list(nx.simple_cycles(ddc))
    cycles_arcs = []
 
    for node_list in cycle_nodes:
        cycle = []
        for i in range(len(node_list)):
            cycle.append((node_list[i], node_list[(i + 1) % len(node_list)]))
        cycles_arcs.append(cycle)
 
    return cycles_arcs

# Seleciona um arco a ser removido de acordo com o algoritmo de seleção.
#Args: ddc (networkx.DiGraph): Grafo direcionado. md_cycle (list): Lista de ciclos.
# Returns: tuple: O arco selecionado para remoção.
def select_arc(ddc, md_cycle):
    arc = {}
    for cycle in md_cycle:
        for a in cycle:
            if a not in arc.keys():
                arc[a] = 1
            else:
                 arc[a] += 1
 
    max_arcs = [a for a in arc if arc[a] == max(arc.values())]
    while(len(max_arcs) > 1):
        fan_out, dummy = class_metrics(ddc, max_arcs[0][0])
        dummy, fan_in = class_metrics(ddc, max_arcs[0][1])
 
        f_out, dummy = class_metrics(ddc, max_arcs[1][0])
        dummy, f_in = class_metrics(ddc, max_arcs[1][1])
        if(fan_out > f_out):
            max_arcs.pop(1)
        elif(f_out > fan_out):
            max_arcs.pop(0)
        elif(fan_out == f_out and fan_in > f_in):
            max_arcs.pop(1)
        elif(fan_out == f_out and f_in > fan_in):
            max_arcs.pop(0)
        else:
            return(max_arcs[0])
    return max_arcs[0]
 
# Realiza o algoritmo guloso de conjunto máximo de arcos de feedback (MFS) em um grafo direcionado.
# Args: ddc (networkx.DiGraph): Grafo direcionado.
# Returns: list: Lista de arcos no conjunto máximo de arcos de feedback.
def mfs_greedy(ddc):
    if ddc is None or not nx.is_directed(ddc):
        return None
 
    mfs = []
    md_cycles = find_minimum_dependency_cycles(ddc)
 
    while len(md_cycles) > 0:
 
        arc = select_arc(ddc, md_cycles)
 
        for i in range(len(md_cycles)-1, -1, -1):
            if arc in md_cycles[i]:
                md_cycles.pop(i)
 
        mfs.append(arc)      
 
    return mfs
