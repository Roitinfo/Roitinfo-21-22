#!/usr/bin/env python
# coding: utf-8

# In[33]:


from manim import *
from manim_editor import PresentationSectionType
import itertools

param = " -v WARNING "


# In[2]:


class DirectedGraph(Graph):
    def __init__(self, vertices, edges, vertex_config=None, **kwargs):
        super().__init__(vertices, edges, **kwargs, vertex_config = vertex_config)
        
        for e in self.edges.values():
            e.add_tip(tip_length=0.2)
        
        self.node_radius = 0
        if (vertex_config is not None and "radius" in vertex_config.keys()):
            self.node_radius = vertex_config["radius"]
            
        
        def edges_updater(graph):
            for (u,v), e in graph.edges.items():
                center_u = graph[u].get_center()
                center_v = graph[v].get_center()
                d = (center_u - center_v)/np.linalg.norm(center_u - center_v)*graph.node_radius
                e.put_start_and_end_on(center_u - d, center_v + d)
                e.pop_tips()
                e.add_tip(tip_length=0.2)
                
        self.clear_updaters()   
        self.add_updater(edges_updater)
        self.update()


# In[3]:


graphs = {
    "intro" : {
        "vertices" : list(range(5)),
        "edges" : [(0, 1), (1, 2), (2, 0), (2, 3), (2, 4), (0, 4)],
    },
    "acyclic" : {
        "vertices" : list(range(5)),
        "edges" : [(0, 1),(1, 2),(2, 3),(2,4)]
    },
    "unconnected" : {
        "vertices" : list(range(5)),
        "edges" : [(0, 1), (1, 2), (0, 2), (3, 4)]
    },
    "tree":{
        "vertices" : list(range(6)),
        "edges" : [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    },
    "treetovis":{
        "vertices" : list(range(7)),
        "edges" : [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    },
    "tobfs":{
        "vertices" : list(range(8)),
        "edges" : [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (3, 4), (4, 5), (1, 6), (5, 7), (4, 6), (6, 7)]
    }
}

global_vertex_config = {"radius":0.3}


# In[5]:


#%%manim $param slide1

class slide1(Scene):
    def construct(self):
        self.next_section("Slide1", type=PresentationSectionType.NORMAL)
        tit = Tex("Grafi").scale(1.5).shift(UP*3)
        self.play(Write(tit))
        gconfig = graphs["intro"]
        graph = Graph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "planar")
        self.play(Create(graph))
        self.wait(0.2)
        self.play(graph.animate.change_layout("circular").shift(LEFT*3))
        
        desc = VGroup(Tex("$V = \{0, 1, 2, 3, 4\}$"),
                      Tex("$E = \{(0,1), (1, 2), (0, 2)...\}$")).arrange(DOWN, buff=1).shift(RIGHT*3).scale(1.2)
        self.play(Write(desc, run_time=0.3))
        self.wait()


# In[6]:


#%%manim $param slide2

class slide2(Scene):
    def construct(self):
        self.next_section("Slide2", type=PresentationSectionType.NORMAL)
        directed = Tex("Diretto").scale(1.5)
        undirected = Tex("Non Diretto").scale(1.5)
        directed.move_to([config["frame_width"]*1/4, 3, 0])
        undirected.move_to([config["frame_width"]*-1/4, 3, 0])
        line = Line([0, config["frame_height"]/2, 0], [0, -config["frame_height"], 0])
        self.play(Create(line), run_time=0.3)
        self.play(Write(directed), Write(undirected), run_time=0.3)
        
        gconfig = graphs["intro"]
        graph1 = Graph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([config["frame_width"]*-1/4, -1, 0])
        graph2 = DirectedGraph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([config["frame_width"]*1/4, -1, 0])
        self.play(Create(graph1), Create(graph2))
        self.wait()
        
        self.next_section("Direziona", type=PresentationSectionType.NORMAL)
        dedges = gconfig["edges"] + [(v, u) for (u, v) in gconfig["edges"]]
        graph3 = DirectedGraph(gconfig["vertices"], dedges, labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([config["frame_width"]*-1/4, -1, 0])
        
        self.play(FadeIn(graph3), run_time=0.3)
        self.wait()


# In[34]:


#%%manim $param slide3

class slide3(Scene):
    def construct(self):
        self.next_section("Slide3", type=PresentationSectionType.NORMAL)
        cyclic = Tex("Ciclico").scale(1.5)
        acyclic = Tex("Aciclico").scale(1.5)
        acyclic.move_to([config["frame_width"]*1/4, 3, 0])
        cyclic.move_to([config["frame_width"]*-1/4, 3, 0])
        line = Line([0, config["frame_height"]/2, 0], [0, -config["frame_height"], 0])
        self.play(Create(line), run_time=0.3)
        self.play(Write(cyclic), Write(acyclic), run_time=0.3)

        gconfig1 = graphs["intro"]
        gconfig2 = graphs["acyclic"]
        graph1 = Graph(gconfig1["vertices"], gconfig1["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([config["frame_width"]*-1/4, -1, 0])
        graph2 = Graph(gconfig2["vertices"], gconfig2["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([config["frame_width"]*1/4, -1, 0])
        self.play(Create(graph1), Create(graph2))
        self.wait()
        
        self.next_section("Cicli1", type=PresentationSectionType.NORMAL)
        self.play(Unwrite(cyclic), Unwrite(acyclic), Uncreate(graph2), Uncreate(line), run_time=0.3)
        
        cycle = Tex("Cicli semplici").shift(UP*3).scale(1.5)
        graph = graph1
        self.play(graph.animate.move_to([0, -1, 0]))
        ed = [(0,1), (1, 2), (2, 0)]
        self.play(*[graph.edges[e].animate.set_color(RED) for e in ed], run_time=0.3)
        self.play(Write(cycle), run_time=0.3)
        self.wait()
        
        self.next_section("Cicli2", type=PresentationSectionType.NORMAL)
        ned = [(2, 0), (0,4), (2,4)]
        self.play(*[e.animate.set_color(RED) for v, e in graph.edges.items() if v in ned and v not in ed],
                  *[e.animate.set_color(WHITE) for v, e in graph.edges.items() if v in ed and v not in ned], run_time=0.3)
        
        self.wait()
        
        self.next_section("Cicli3", type=PresentationSectionType.NORMAL)
        ed = ned
        ned = [(1, 2), (0, 1), (0, 4), (2, 4)]
        self.play(*[e.animate.set_color(RED) for v, e in graph.edges.items() if v in ned and v not in ed],
                  *[e.animate.set_color(WHITE) for v, e in graph.edges.items() if v in ed and v not in ned], run_time=0.3)
        self.wait()
        self.next_section("Cicli4", type=PresentationSectionType.NORMAL)
        
        self.remove(graph)
        graph = DirectedGraph(gconfig1["vertices"], gconfig1["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([0, -1, 0])
        self.add(graph)
        
        ed = [(0,1), (1, 2), (2, 0)]
        self.play(*[graph.edges[e].animate.set_color(RED) for e in ed], run_time=0.3)
        self.wait()
        self.next_section("skip", type=PresentationSectionType.SKIP)
        self.play(Unwrite(cycle), Uncreate(graph), run_time = 0.2)
        self.wait()


# In[36]:


#%%manim $param slide4

class slide4(Scene):
    def construct(self):
        self.next_section("Slide4", type=PresentationSectionType.NORMAL)
        connected = Tex("Connesso").scale(1.5)
        unconnected = Tex("Non Connesso").scale(1.5)
        unconnected.move_to([config["frame_width"]*1/4, 3, 0])
        connected.move_to([config["frame_width"]*-1/4, 3, 0])
        line = Line([0, config["frame_height"]/2, 0], [0, -config["frame_height"], 0])
        self.play(Create(line), run_time=0.3)
        self.play(Write(connected), Write(unconnected), run_time=0.3)

        gconfig1 = graphs["intro"]
        gconfig2 = graphs["unconnected"]
        graph1 = Graph(gconfig1["vertices"], gconfig1["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([config["frame_width"]*-1/4, -1, 0])
        graph2 = Graph(gconfig2["vertices"], gconfig2["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([config["frame_width"]*1/4, -1, 0])
        self.play(Create(graph1), Create(graph2))
        self.wait()
        self.next_section("Componenti", type=PresentationSectionType.NORMAL)
        self.play(Unwrite(connected), Unwrite(unconnected), Uncreate(graph1), Uncreate(line), run_time=0.3)
        
        
        graph = graph2
        a1 = [0, 1, 2]
        a2 = [3, 4]
        c1 = VGroup(*[graph[x] for x in a1], *[graph.edges[(u, v)] for u,v in itertools.product(a1, repeat=2) if (u,v) in graph.edges.keys()])
        c2 = VGroup(*[graph[x] for x in a2], *[graph.edges[(u, v)] for u,v in itertools.product(a2, repeat=2) if (u,v) in graph.edges.keys()])
        c = VGroup(c1, c2)
        self.play(graph.animate.move_to([0, -1, 0]))
        comp = Tex("Componenti connesse").shift(UP*3).scale(1.5)
        self.play(Write(comp), run_time=0.3)
        self.play(c.animate.arrange())
        self.wait()
        self.next_section("skip", type=PresentationSectionType.SKIP)
        self.play(Unwrite(comp), Uncreate(graph), run_time=0.2)
        self.wait()
     


# In[34]:


#%%manim $param slide5

class slide5(Scene):
    def construct(self):
        self.next_section("Slide5", type=PresentationSectionType.NORMAL)
        trees = Tex("Alberi").shift(UP*3).scale(1.5)
        self.play(Write(trees), run_time=0.2)
        
        gconfig = graphs["tree"]
        gconfig["vertices"] = [0, 4, 1, 3, 2, 5]
        tree = Graph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([0, -1, 0])
        self.play(Create(tree))
        self.wait()
        self.next_section("Radice", type=PresentationSectionType.NORMAL)
        self.play(tree.animate.change_layout("tree", root_vertex = 0))
        self.wait()
        self.next_section("Skip", type=PresentationSectionType.SKIP)
        self.play(Unwrite(trees), Uncreate(tree), run_time=0.2)
        self.wait()

# In[62]:


#%%manim $param slide6

class slide6(Scene):
    def construct(self):
        self.next_section("slide6", type=PresentationSectionType.NORMAL)
        percorsi = Tex("Percorsi").shift(UP*3).scale(1.5)
        
        
        gconfig = graphs["intro"]
        graph =Graph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([0, -1, 0])
        self.play(Create(graph))
        self.play(Write(percorsi), run_time=0.2)
        
        ed1 = [(1, 2), (2, 4)]
        ed2 = [(0, 1), (0, 4)]
        
        edo1 = VGroup(*[l.copy().add_tip(tip_length=0.2) for (u, v), l in graph.edges.items() if (u,v) in ed1]).set_color(RED).set_z_index(2).set_stroke(width = 10)
        edo2 = VGroup(*[l.copy().add_tip(tip_length=0.2) for (u, v), l in graph.edges.items() if (u,v) in ed2]).set_color(GREEN).set_z_index(2).set_stroke(width = 10)
        edo2[0].rotate(PI)
        self.play(Create(edo1), run_time=0.2)
        self.wait()
        self.next_section("percorso2", type=PresentationSectionType.NORMAL)
        self.play(Create(edo2), run_time=0.2)
        self.wait()
        self.play(Unwrite(percorsi), Uncreate(graph), Uncreate(edo1), Uncreate(edo2), run_time=0.2)
        self.wait()


# In[170]:


#%%manim $param slide7

class slide7(Scene):
    def construct(self):
        self.next_section("slide7", type=PresentationSectionType.NORMAL)
        tit = Tex("Liste di Archi").scale(1.5).shift(UP*3)
        gconfig = graphs["intro"]
        graph =Graph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular").move_to([3, -1, 0])
        self.play(Create(graph))
        self.play(Write(tit), run_time=0.2)
        
        lis = VGroup(*[Tex("(", u, ";", v,")").arrange(buff = 0.2).scale(1.5) for (u, v), e in graph.edges.items()]).arrange_in_grid(cols=2, buff=1).shift(LEFT*3 + DOWN)
        self.play(Write(lis), run_time=0.2)
        self.wait()
        self.next_section("liste", type=PresentationSectionType.NORMAL)
        self.play(Unwrite(lis), Unwrite(tit), run_time=0.2)
        
        tit = Tex("Liste di Adiacenza").scale(1.5).shift(UP*3)
        self.play(Write(tit), run_time=0.2)
        
        
        lis = VGroup(*[Tex(f"{x}: ", *([str(u) + ", " for (u, v), e in graph.edges.items() if v == x] + [str(v) + ", " for (u, v), e in graph.edges.items() if u == x])).scale(1.5) for x in graph.vertices]).arrange(DOWN, buff=0.5).shift(LEFT*3 + DOWN/2)
        for i in range(5):
            lis[i][0].set_color(YELLOW)
            lis[i].shift(lis[i].get_corner([1, 1, 0])*np.array([1, 0, 0]))

        self.play(Write(lis), run_time=0.3)
        self.wait()
        self.next_section("matrici", type=PresentationSectionType.NORMAL)
        self.play(Unwrite(tit), Unwrite(lis), run_time=0.2)
        
        tit = Tex("Matrice di Adiacenza").scale(1.5).shift(UP*3)
        self.play(Write(tit), run_time=0.2)
        s = 0.7
        t = s*6
        grid = VGroup(*[Line([0, s*y, 0], [t, s*y, 0]) for y in range(7)], *[Line([s*x, 0, 0], [s*x, t, 0]) for x in range(7)])
        grid.add(*[Tex(str(i)).move_to([(i+1.5)*s, t-s*0.5, 0]) for i in graph.vertices])
        grid.add(*[Tex(str(i)).move_to([0.4, t-(i+1.5)*s, 0]) for i in graph.vertices])
        i = len(grid)
        grid.add(*[Square().scale(s/2).move_to([1+u*s+0.05, t-1-v*s-0.05, 0]).set_fill(opacity=0.5, color=GREEN) for (u, v), e in graph.edges.items()])
        grid.add(*[Square().scale(s/2).move_to([1+v*s+0.05, t-1-u*s-0.05, 0]).set_fill(opacity=0.5, color=GREEN) for (u, v), e in graph.edges.items()])
        grid.shift(DOWN*3+LEFT*5)
        self.play(Create(grid[:i]), run_time=0.4)
        self.play(FadeIn(grid[i:]), run_time=0.2)
        self.wait()
        self.next_section("skip", type=PresentationSectionType.SKIP)
        self.play(Uncreate(graph), Uncreate(grid[::-1]), Unwrite(tit), run_time=0.2)
        self.wait()


# In[176]:


#%%manim $param slide8

class slide8(Scene):
    def construct(self):
        self.next_section("slide8", type=PresentationSectionType.NORMAL)
        quest = VGroup(Tex("Il grafo è connesso?"), Tex("Quante sono le componenti?"), Tex("Qual'è il percorso minimo fra due nodi?")).scale(1.5).arrange(DOWN, buff=1)
        self.play(Write(quest), run_time=0.4)


# In[38]:


#%%manim $param slide9

class slide9(Scene):
    def construct(self):
        self.next_section("slide9", type=PresentationSectionType.SKIP)
        tit = Tex("BFS e DFS").shift(UP*3).scale(1.5)
        self.play(Write(tit), run_time=0.2)
        gconfig = graphs["treetovis"]
        tree1 =Graph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "tree", root_vertex=0).move_to([-3, -1, 0])
        tree2 = tree1.copy().shift(RIGHT*6)
        self.play(Create(tree1), Create(tree2))
        
        self.next_section("Loop", type=PresentationSectionType.LOOP)
        l1 = [(0, 2), (0, 1), (2, 6), (2, 5), (1, 4), (1, 3)]
        l2 = [(0, 2), (2, 6), (2, 5), (0, 1), (1, 4), (1, 3)]
        
        for n in tree1.vertices.values():
            n.set_z_index(2)        
        for n in tree2.vertices.values():
            n.set_z_index(2)
        
        for i in range(len(l1)):
            a1, a2 = tree1.edges[l1[i]].copy().set_color(GREEN).set_z_index(1).set_stroke(width=10), tree2.edges[l2[i]].copy().set_color(GREEN).set_z_index(1).set_stroke(width=10)
            self.play(Create(a1), Create(a2), run_time=1)


# In[41]:


#%%manim $param slide10

class slide10(Scene):
    def construct(self):
        self.next_section("Slide10", type=PresentationSectionType.NORMAL)
        tit = Tex("BFS").scale(1.5).shift(UP*3)
        gconfig = graphs["tobfs"]
        graph =Graph(gconfig["vertices"], gconfig["edges"], labels=True, vertex_config = global_vertex_config, layout = "circular", layout_scale=2.5).move_to([-3, -1, 0])
        self.play(Create(graph))
        self.play(Write(tit))
        
        for n in graph.vertices.values():
            n.set_z_index(2)
            
        q = VGroup()
        sq = Square().shift(RIGHT*3+DOWN*2.5).scale(0.5)
        self.play(Create(sq), run_time=0.2)
        
        def add(x):
            t = Tex(x).scale(2).next_to(q, UP)
            if (len(q) == 0):
                t.shift(RIGHT*3+DOWN*3)
            t.shift(UP)
            q.add(t)
            self.play(FadeIn(t), t.animate.shift(DOWN), graph[x].animate.set_color(YELLOW), run_time=0.2)
        
        def pop(x):
            e = q[0]
            q.remove(e)
            self.play(e.animate.shift(DOWN).set_fill(opacity=0), graph[x].animate.set_color(GREEN), run_time=0.2)
            e.shift(UP)
            self.play(q.animate.shift((e.get_corner([-1, -1, 0]) - q.get_corner([-1, -1, 0]))*np.array([0, 1, 0])), run_time=0.2)
            
        
        
        vis = [False] * len(graph)
        tovis = [False] * len(graph)
        queue = [0]
        l = graph[0][1].copy().set_z_index(3)
        self.add(l)
        add(0)
        while(len(queue) > 0):
            x = queue.pop(0)
            vis[x] = True
            self.next_section("Vis" + str(x), type=PresentationSectionType.NORMAL)
            
            for (u, v), e in graph.edges.items():
                if (x != u and x != v):
                    continue
                y = u
                if (x == u):
                    y = v
                if (vis[y]):
                    continue

                a = e.copy().set_color(GREEN).set_stroke(width=10).set_z_index(1)
                if (x == v):
                    a.rotate(PI)
                self.play(Create(a), run_time=0.3)
                if not tovis[y]:
                    self.next_section("Add" + str(y), type=PresentationSectionType.NORMAL)
                    l = graph[y][1].copy().set_z_index(3)
                    self.add(l)
                    l.set_color(BLACK)
                    tovis[y] = True
                    queue.append(y)
                    add(y)
            pop(x)
        self.wait()


# In[ ]:




