import networkx as nx


def valid_word(g, s, t, w):
    if g is None or s is None or t is None or w is None:
        return None
    if not (s in g.nodes and t in g.nodes):
        return None
    if not isinstance(w, str):
        return None

    pilha = [(s, w)]
    while pilha:
        u, palavra = pilha.pop()
        if u == t and len(palavra) == 0:
            return True
        if u not in g:
            continue
        for v, d in g[u].items():
            if not d:
                continue
            for edge in d.values():
                label = edge.get('label', '')
                if label == palavra[:len(label)]:
                    pilha.append((v, palavra[len(label):]))
    return False
