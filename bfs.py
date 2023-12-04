def BFS(G,s):
    return 0

class Node:
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
    def __init__(self,norp) -> None:
        self.n = norp
        self.m = 0
        self.vertices = [ DLL(Node(i)) for i in range(1,norp+1)]
    def addEdge(self,u,v):#edge = touple of structure (x,y), where  1<=x,y<=n.
        self.vertices[u-1].addNode(Node(v))
    def printVertexEdges(self,u):
        #assumption: 1<=u<=n
        vertDll = self.vertices[u-1]
        p = vertDll.head
        while p is not None:
            print(f' ({u},{p.value})')
            p=p.prev
        
dag1 = DAGraph(5)
dag1.addEdge(1,2)
dag1.addEdge(1,3)
dag1.addEdge(1,5)
dag1.printVertexEdges(1)