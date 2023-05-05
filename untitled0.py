
from collections import deque    # Módulo de mesa lineal

class Graph(object):
    def __init__(self, *args, **kwargs):
        self.order = []  # orden
        self.neighbor = {}
 
    def add_node(self, node):
        key, val = node
        if not isinstance(val, list):
            print('La entrada del nodo debe ser una tabla lineal')    # Evite la entrada incorrecta
        self.neighbor[key] = val
 
    # Implementación del algoritmo de anchura primero
    def BFS(self, root):
        # Determina si el nodo raíz está vacío
        if root != None:
            search_queue = deque()
            search_queue.append(root)
            visited = []
        else:
            print('root is None')
            return -1
 
        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)
 
            if (not person in visited) and (person in self.neighbor.keys()):
                search_queue += self.neighbor[person]
                visited.append(person)
 
    # Implementación del algoritmo de profundidad primero
    def DFS(self, root):
        # Primero determine si el nodo raíz es un nodo vacío
        if root != None:
            search_queue = deque()
            search_queue.append(root)
 
            visited = []
        else:
            print('root is None')
            return -1
 
        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)
 
            if (not person in visited) and (person in self.neighbor.keys()):
                tmp = self.neighbor[person]
                tmp.reverse()
 
                for index in tmp:
                    search_queue.appendleft(index)
 
                visited.append(person)
 
    def clear(self):
        self.order = []
 
    def node_print(self):
        for index in self.order:
            print(index, end='  ')
 
   
    
if __name__ == '__main__':
   # Crea un gráfico de árbol binario
    g = Graph()
    g.add_node(('S', ['D', 'G']))
    g.add_node(('S', ['A','B','C','G']))
    g.add_node(('S', ['A','B','G']))
    g.add_node(('S', ['D','G']))
    # Realice una búsqueda en amplitud
    g.BFS('S')
    print('Busqueda por anchura:')
    print('  ', end='  ')
    g.node_print()
    g.clear()
 
 