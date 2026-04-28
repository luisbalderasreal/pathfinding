from numpy import inf

class IDAStarSolver:
    def __init__(self, T):
        self.T = T
        self.start = None
        self.target = None
        self.P = {}
    
    def solve(self, start = None, target = None):
        
        P = {}
        
        if not start:
            start = self.T.random_start()
        if not target:
            target = self.T.default_target
        
        self.start = start
        self.target = target
        self.P[start] = None
        
        bound = self.T.heuristic(self.start, self.target)
        while True:
            result = self.ida(self.start, 0, bound)
            if result == 'found':
                self.T.print_path(self.target, self.P)
                return
            elif result == inf:
                print("No path found.")
                return
            elif result >= self.T.max_depth(self.start):
                print("Maximum depth reached.")
                return
            bound = result
    
    def ida(self, node, node_dist, bound):
        f = node_dist + self.T.heuristic(node, self.target)
        if f > bound:
            return f
        if node == self.target:
            return 'found'
        minim = inf
        for (next_node, next_cost) in self.T.neighbors(node):
            b = self.ida(next_node, node_dist+next_cost, bound)
            if b == 'found':
                self.P[next_node] = node
                return 'found'
            if b < minim:
                minim = b
        return minim