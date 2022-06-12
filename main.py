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
            just_moved = True
            group = VGroup()
            edge = Mobject()
            while(True):
                for e in g_visual.edges:
                    if (v in e) and (ancestors[v] in e):
                        edge = g_visual.edges[e]
                graph[v] = remove_visited(graph[v], visited)
                group = VGroup()
                for node in graph[v]:
                    for e in g_visual.edges:
                        if (node in e) and (v in e):
                            group.append_vectorized_mobject(g_visual.edges[e])
                            break
                if (just_moved):
                    self.play(
                        dot.animate.move_to(g_visual.vertices[v]),
                    )
                if not(visited[v]):

                    self.play(
                        AnimationGroup(
                            group.animate.set_color(ORANGE),
                            g_visual.vertices[v].animate.set_color(BLUE),
                            Flash(g_visual.vertices[v], color=BLUE),
                            edge.animate.set_color(BLUE)
                        )
                    )
                just_moved = False
                visited[v] = True

                if (graph[v]):

                    new_v = graph[v].pop()
                    ancestors[new_v] = v
                    v = new_v
                    just_moved = True

                else:
                    v = ancestors[v]
                    just_moved = True
                    if not(v):
                        break
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
