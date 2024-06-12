from queue import *

def read_graph(f):
    """Read a graph from a file object 'f' (text) containing one
    vertex and its adjacency list per line.  E.g.:

    Input:     | Graph:
    A B C      |  A --> B
    B C        |  |    /^
    C B        |  v   / |
               |  C<-/  /
               |   ^---/

    Return three containers:

    V: (array) Vertex Id -> Vertex Name
    Adj: (array) Vertex Id -> array of Vertex Id
    V_idx: (dictionary) Vertex Name -> Vertex Id
    """
    V = []
    Adj = []
    V_idx = {}
    for line in f:              # for each line in the input f
        l = line.split()
        assert len(l) > 0
        v_name = l[0]           # v_name is the source vertex
        if v_name in V_idx:     # We already have vertex v_name
            v = V_idx[v_name]
        else:
            v = len(V)          # Add vertex at the end of V, Adj
            V_idx[v_name] = v
            V.append(v_name)
            Adj.append([])
        for i in range (1, len(l)):
            u_name = l[i]       # u_name is a target vertex
            if u_name in V_idx: # We already have vertex u_name
                u = V_idx[u_name]
            else:               # Add vertex, as above
                u = len(V)
                V_idx[u_name] = u
                V.append(u_name)
                Adj.append([])
            Adj[v].append(u)

    return V, Adj, V_idx


def minimal_additional_edges(G):
    """Takes in an undirected graph G. Returns the minimal number of edges that
    must be added to G to make it connected.
    Works by running a BFS and marking which nodes have been visited. On each iteration
    of BFS a connected component is counted.
    Additional edges equal the number of connected components minus one."""
    n = len(G)
    all_vertices = set(range(n))
    visited_vertices = set()
    connected_components = 0
    while all_vertices != visited_vertices:
        connected_components += 1
        # get a start vertex which has not been visited yet
        for el in all_vertices:
            if el not in visited_vertices:
                start = el
                break
        # run BFS to mark all connected vertices as visited
        g = Queue()
        g.put(start)
        visited_vertices.add(start)
        while not g.empty():
            u = g.get()
            for v in G[u]:
                if v not in visited_vertices:
                    g.put(v)
                    visited_vertices.add(v)
    return connected_components - 1
