import networkx as nx


def is_candidate(g, q_list, q, t):
    if t < 0:
        return None
    if q not in q_list:
        return False
    elif q in q_list:
        return None
    
    for v in q_list:
        if nx.has_path(g, v, q):
            return False
    
    for v in q_list:
        if nx.shortest_path_length(g, v, q) > t:
            return False
        
        elif nx.shortest_path_length(g, q, v) > 0 and nx.shortest_path_length(g, q, v) <= t:
            return True
