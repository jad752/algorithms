"""
Contains basic classes for holding graph information.
"""

VID = 0
ALIST = 1

NOT_DISCOVERED = -1
NOT_FINISHED = -1

test_graph = [
                [1, [2, 3, 4]],
                [2, [9, 10]],
                [3, [7, 8]],
                [4, [5, 6]],
                [10, [11, 12]],
             ]

class Vertex():
    """
    The nodes in our graph.
    """
    def __init__(self, vid):
        """
            Args:
                vid: this node's id

            Returns:
                None
        """
        self.vid = vid
        self.color = None
        self.pred = None
        self.discover = NOT_DISCOVERED
        self.finish = NOT_FINISHED
        self.neighbors = []

    def __eq__(self, other):  # we override equal to just check vid
       return self.vid == other.vid

    def __str__(self):
        return str(self.vid)

    def __hash__(self):
        return self.vid


class Edge():
    """
    The edges of our graph.
    """
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return str(self.v1) + "<-->" + str(self.v2)

    def get_vertices(self):
        return (self.v1, self.v2)

    def is_incident(self, v):
        return (v == self.v1) or (v == self.v2)


def extract_vertex_set(edges):
    """
    Returns a set of all the vertices in the edge collection.
    """
    vertices = set()
    for e in edges:
        (u, v) = e.get_vertices()
        vertices.add(u)
        vertices.add(v)
    return vertices


class Graph():
    """
    The graph structure.
    """

    def __init__(self, alist):
        """
        Args:
            alist: a list of ints for the nodes and a list of what they are
            connected to.
        """
        # the following item is a heterogeneous list. The first item is a node,
        # but the rest of the items are just node ids.
        self.vertices = None
        self.edges = []

        for v in alist:
            vid = v[VID]

            for uid in v[ALIST]:
                add_edge(vid, uid)

        if not self.isconnected():
            print("Warning: these algorithms only work on connected graphs, "
                  + "but this graph is not connected.")

    def __str__(self):
        s = ''
        for e in self.edges:
            s += str(e) + "\n"
        return s

    def add_vertex(self, vid):
        if vid not in self.vertices:
            self.vertices.add(Vertex(vid))

    def add_edge(self, vid, uid):
        """
            We can safely add these vertices, because we check for dups
            before adding.
        """
        self.add_vertex(vid)
        self.add_vertex(uid)
        self.edges.append(Edge(vid, uid))

    def isconnected(self):
        return True

    def get_vertex(self, vid):
        return self.vertices[vid]

    def get_alist(self, vid):
        if vid in self.adj_lists:
            return self.adj_lists[vid][ALIST:]
        else:
            return None

    def get_edges(self):
        return self.edges

    def get_vertices(self):
        return self.vertices

    def iscover(self, edges):
        """
        See if this edge set is a vertex cover.
        Return:
            True if it is, False if not.
        """
        cover_set = extract_vertex_set(edges)
        for e in self.edges:
            (u, v) = e.get_vertices
            if u not in cover_set and v not in cover_set:
                return False
        return True

