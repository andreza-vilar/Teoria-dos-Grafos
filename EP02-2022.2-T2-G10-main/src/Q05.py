import networkx as nx


def change_costs_factor(ddc, c):
    if ddc is None or not ddc.has_node(c):
        return None
    if not nx.is_directed(ddc):
        return None
    
    # Custo de manuntenção
    fator = 1
    
    # Verificar se outras classes são dependentes de c
    dependente = [node for node in ddc.nodes() if node!=c and nx.has_path(ddc, node, c)]
    fator += len(dependente)

    # Verifica se a classe faz parte de algum tangle
    tangle = [comp for comp in nx.strongly_connected_components(ddc) if len(comp) > 3]
    for tangle in tangle:
        if c in tangle:
            fator += 50
            break
    # Verifica se a classe faz parte de ciclos de minima dependência
    ciclos = list(nx.simple_cycles(ddc))
    ciclos_minimos = []
    for ciclos in ciclos:
        if c in ciclos:
            ciclos_minimos.append(ciclos)
    fator += len(ciclos_minimos) * 10

    return fator
