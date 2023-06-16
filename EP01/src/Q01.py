import networkx as nx


def associate_astronauts(list_a):  # Elementos da lista: (name,surname,country)
    # Garante que a entrada é uma lista de tuplas
    if not isinstance(list_a, list) or any(not isinstance(astronaut, tuple) or len(astronaut) != 3 for astronaut in list_a):
        return None
    G = nx.Graph()
    
    #Adicionando os vértices
    for index, astronaut in enumerate(list_a):
        G.add_node(index, first_name = astronaut[0], last_name = astronaut[1], country = astronaut[2])

    # Adiciona as arestas
    for c, astronaut1 in enumerate(list_a):
        for j, astronaut2 in enumerate(list_a):
            if astronaut1[2] != astronaut2[2]:
                G.add_edge(c,j)
    
    return G