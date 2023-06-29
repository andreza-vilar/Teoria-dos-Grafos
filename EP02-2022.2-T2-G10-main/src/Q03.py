import networkx as nx

def dependencies(ddc, c):

    # verifica se o grafo é nulo
    if ddc is None:
        return None
    
    # verifica se C está contido no grafo
    if c not in ddc:
        return None
    
    # verifica se o grafo é tipo nc.digraph
    if not isinstance(ddc, nx.DiGraph):
        return None
    
    # inicializa as listas de dependências diretas e indiretas
    direct_dependencies = list(ddc.successors(c))
    indirect_dependencies = []

    # verifica as dependências indiretas
    for n in direct_dependencies:
        candidates = list(ddc.successors(n))
        for e in candidates:
            # ignora se houver elementos duplicados
            if e == c:
                continue
            # adiciona o elemente como dependência indireta
            if e not in direct_dependencies:
                indirect_dependencies.append(e)
    
    for n in indirect_dependencies:
        candidates = list(ddc.successors(n))
        for e in candidates:
            if e == c:
                continue
            if e not in direct_dependencies and e not in indirect_dependencies:
                indirect_dependencies.append(e)

    # remove duplicatas das dependências indiretas
    for n in indirect_dependencies:
        if (indirect_dependencies.count(n) > 1):
            indirect_dependencies.remove(n)
    
    return direct_dependencies, indirect_dependencies
