import queue
def BFS(G,s=1):
    # for i in range(1,G.n+1):
    #     vert = G.vertices[i-1]
    #     print(f'\nVert {i} color is {vert.colour}, its distance is {vert.d}, and its PI is {vert.PI}')
    vertex_s = G.vertices[s-1]
    vertex_s.colour = "grey" #was "white"
    vertex_s.d = 0 #was infinity
    Q = queue.Queue()
    Q.put(vertex_s) #enqueue
    while Q.empty() is False:
        u = Q.get() #dequeue
        neighbourTraverser = u.neighbours.head
        while neighbourTraverser is not None:
            v = neighbourTraverser.value
            vertex_neighbour = G.vertices[v-1]
            if vertex_neighbour.colour is "white":
                vertex_neighbour.colour = "grey"
                vertex_neighbour.d = u.d+1
                vertex_neighbour.PI = u
                Q.put(vertex_neighbour)
            neighbourTraverser = neighbourTraverser.prev
        u.colour = "black"

def printVertexBFSData(G):
    for i in range(1,G.n+1):
        vert = G.vertices[i-1]
        print(f'\nVert {i} color is {vert.colour}, its distance is {vert.d}, and its PI is {vert.PI}')

############################ Graph Data Structure and accessory structures #############################
class DLLNode:#is a DLL Node.
    def __init__(self,value,next = None) -> None:
        self.value = value
        self.next = None
        self.prev = None
class DLL:
    def __init__(self,first = None) -> None:
        self.head = first
    def addNode(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            self.head.next = newNode
            newNode.prev = self.head
            self.head = newNode

class DAGraph:
    def __init__(self,norp,directed = False) -> None:
        self.n = norp
        self.m = 0
        self.directed = directed
        self.vertices = [ Vertex() for i in range(1,norp+1)]
    def addEdge(self,u,v):
        self.vertices[u-1].neighbours.addNode(DLLNode(v))
        if self.directed is False:
            self.vertices[v-1].neighbours.addNode(DLLNode(u))
    def printVertexEdges(self,u):
        #assumption: 1<=u<=n
        vertDll = self.vertices[u-1].neighbours
        p = vertDll.head
        while p is not None:
            print(f' ({u},{p.value})')
            p=p.prev
    def printGraph(self):
        for x in range(1,self.n+1):
            self.printVertexEdges(x)

class Vertex:
    def __init__(self) -> None:
        self.d = float("inf")
        self.PI = None
        self.colour = "white"
        self.neighbours = DLL()

############################ MAIN | #############################
#                                 V                             #
dag1 = DAGraph(5,True)
dag1.addEdge(1,2)
dag1.addEdge(1,3)
dag1.addEdge(1,5)
dag1.addEdge(2,4)
dag1.addEdge(2,5)
dag1.addEdge(3,4)
dag1.addEdge(5,3)
dag1.printGraph()
BFS(dag1)
printVertexBFSData(dag1)