from random import choices, randint
from math import floor

class AbbaCode:
    
    def __init__(self, coding):
        self.coding = coding
        self.best_rate = min(len(zero1)/len(ab) for ab, zero1 in coding.items())
        self.worst_rate = min(len(zero1)/len(ab) for ab, zero1 in coding.items())
    
    default_target = ''
        
    @classmethod
    def random_start(cls):
        random_length = randint(7, 13)
        random_list = choices(['a', 'b'], k = random_length)
        return ''.join(random_list)
    
    def neighbors(self, seq):
        neighborList = []
        for ab, zero1 in self.coding.items():
            if seq[:len(ab)] == ab:
                neighborList.append((seq[len(ab):], len(zero1)))
        return neighborList
    
    @classmethod
    def dist(cls, seq, neighbor):
        return 1
    
    def heuristic(self, seq, target):
        return floor(len(seq)*self.best_rate)
    
    def max_depth(self, start):
        return ceil (len(start)*self.worst_rate)
    
    def print_path(self, node, p):
        step = 0
        code = ''
        prev_node = p[node]
        node_len = len(node)
        if prev_node != None:
            step, code = self.print_path(prev_node, p)
            prev_node_len = len(prev_node)
            len_diff = prev_node_len - node_len
            missing = prev_node[:len_diff]
            zero1 = self.coding[missing]
            code = zero1+code
        print(f"{step}\t{node}\tC: {code}")
        step = step+1
        return step, code