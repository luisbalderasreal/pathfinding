from fibonacci_heap import FibonacciHeap

class AStarSolver:
    def __init__(self, T):
        self.T = T
        self.start = None
        self.target = None
        
        # Dictionary with a given node's previous node in path.
        # key: node string
        # value: key's previous node
        self.P = {}
        # Dictionary with node distance from starting node.
        # key: node string
        # value: distance from start node
        self.D = {}
    
    def solve(self, start = None, target = None):
        self.D = {}
        self.P = {}
        
        # Graph nodes already checked.
        # key: node string
        # value: True if node is checked. Otherwise key does not exist.
        checked = {}

        # Fibonacci heap keeping a queue for next graph nodes to check.
        # key: d(v) + h(v)
        # value: node string
        heap = FibonacciHeap()

        # Dictionary with the fibonacci heap nodes.
        # key: graph node string
        # value: fibonacci heap node
        heap_nodes = {}
        
        if not start:
            start = self.T.random_start()
        if not target:
            target = self.T.default_target
        self.start = start
        self.target = target
        
        heap_nodes[self.start] = heap.insert(0, self.start)
        self.D[self.start] = 0
        self.P[self.start] = None

        while True:
            heap_node = heap.extract_min()
            if not heap_node:
                print("No path found.")
                return checked, heap_nodes
            node = heap_node.value
            del heap_nodes[node]
            if node == self.target:
                self.T.print_path(self.target, self.P)
                return checked, heap_nodes
            checked[node] = True

            for (next_node, next_cost) in self.T.neighbors(node):
                if next_node in checked:
                    continue
                elif next_node not in self.D:
                    self.D[next_node] = self.D[node]+next_cost
                    self.P[next_node] = node
                    heap_nodes[next_node] = heap.insert(self.D[next_node]+self.T.heuristic(next_node, self.target), next_node)
                elif self.D[next_node] > self.D[node]+next_cost:
                    self.D[next_node] = self.D[node]+next_cost
                    self.P[next_node] = node
                    heap.decrease_key(heap_nodes[next_node], self.D[next_node]+self.T.heuristic(next_node, self.target))