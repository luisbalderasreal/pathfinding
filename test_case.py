class Test:
    
    @classmethod
    def random_start(cls):
        return 1
    
    @classmethod
    def neighbors(cls, num):
        match num:
            case 1:
                return [(2,1)]
            case 2:
                return [(3,1)]
            case 3:
                return []
            case 4:
                return []
    
    @classmethod
    def heuristic(cls, num, target_num):
        return 1
    
    @classmethod
    def max_depth(cls, start):
        return 3
    
    @classmethod
    def print_path(cls, node, p):
        step = 0
        prev_node = p[node]
        if prev_node != None:
            step = cls.print_path(prev_node, p)
        print(f"{step}\t{node}")
        step = step+1
        return step