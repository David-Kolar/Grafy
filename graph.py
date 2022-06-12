from manim import *
from collections import deque

def make_graph(paths=(), n=0):
    graph = dict()
    for a, b in paths:
        try:
            graph[a]
        except:
            graph[a] = []
        try:
            graph[b]
        except:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def find_edge(graph, v1, v2):
    for edge in graph.edges:
        if (v1 in edge) and (v2 in edge):
            return edge
    return tuple()

def orange_mobjects(graph, v1, other_nodes):
    vertices = []
    edges = []
    for edge in graph.edges:
        if (v1 in edge):
            for node in other_nodes:
                if (node in edge):
                    edges.append(edge)
                    vertices.append(node)
    return edges, vertices

class SaveAndRestoreExample(Scene):
    def construct(self):
        circle = Circle().set_color(WHITE)
        circle.save_state()
        square = Square().set_color(WHITE).set_fill(BLUE, opacity=100)
        self.play(FadeIn(circle))
        self.play(Transform(circle, square))
        self.play(circle.animate.restore())
        self.play(FadeIn(circle))

def remove_visited(nodes, visited):
    ls = []
    for val in nodes:
        if not(visited[val]):
            ls.append(val)
    return ls

class GraphExample(Scene):
    def construct(self):
        def DFS(v):
            dot = Dot().move_to(g_visual.vertices[v]).set_color(BLUE)
            self.play(g_visual.vertices[v].animate.set_color(BLUE), Flash(g_visual.vertices[v], color=BLUE))
            while(True):
                graph[v] = remove_visited(graph[v], visited)

                visited[v] = True

                if (graph[v]):
                    orange_nodes, orange_vertices = orange_mobjects(g_visual, v, graph[v])
                    self.play(
                        *[g_visual.vertices[vertice].animate.set_color(ORANGE) for vertice in orange_vertices],
                        *[g_visual.edges[edge].animate.set_color(ORANGE) for edge in orange_nodes]
                    )
                    new_v = graph[v].pop()
                    ancestors[new_v] = v

                else:
                    new_v = ancestors[v]
                    if not(new_v):
                        break
                old_v = v
                v = new_v
                edge = find_edge(g_visual, v, old_v)
                orange_vertices = [vertice for vertice in orange_vertices if vertice!= v]
                orange_nodes = [node for node in orange_nodes if  node != edge]
                if (visited[v]):
                    self.play(
                        dot.animate.move_to(g_visual.vertices[v]),
                        g_visual.edges[edge].animate.set_color(BLUE)
                    )
                else:
                    self.play(
                        dot.animate.move_to(g_visual.vertices[v]),

                    )
                    self.play(
                        *[g_visual.vertices[vertice].animate.set_color(WHITE) for vertice in orange_vertices],
                        *[g_visual.edges[node].animate.set_color(WHITE) for node in orange_nodes],
                        g_visual.vertices[v].animate.set_color(BLUE),
                        Flash(g_visual.vertices[v], color=BLUE),
                        g_visual.edges[edge].animate.set_color(BLUE)

                    )

        # graf očekává vrcholy a hrany v tomto tvaru
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        edges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (2, 4),
            (2, 5),
            (6, 5),
            (1, 7),
            (5, 7),
            (2, 8),
            (1, 9),
            (10, 8),
            (5, 11),
        ]
        v = 5
        visited = [False for _ in range(vertices[-1]+1)]
        ancestors = [False for _ in range(vertices[-1]+1)]
        g_visual = Graph(vertices, edges, layout_config={"seed": 0}).scale(2)
        graph = make_graph(edges)
        self.play(Write(g_visual))
        DFS(v)
        self.wait(10)
