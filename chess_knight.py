from math import ceil

class Knight:
    
    def __init__(self, obstacles, size_x, size_y):
        self.obstacles = obstacles
        self.size_x = size_x
        self.size_y = size_y
        
    default_target = (0,0)
    
    def neighbors(self, pos):
        neighborList = []
        x = pos[0]
        y = pos[1]
        neighbor_pre_check = [(x-2,y-1),(x-2,y+1),
                             (x-1,y-2),(x-1,y+2),
                             (x+1,y-2),(x+1,y+2),
                             (x+2,y-1),(x+2,y+1)]
        for (x_p, y_p) in neighbor_pre_check:
            if x_p > -1 and x_p < self.size_x and y_p > -1 and y_p < self.size_y and (x_p, y_p) != (x, y) and (x_p, y_p) not in self.obstacles:
                neighborList.append(((x_p, y_p),1))
        return neighborList
    
    def heuristic(self, pos, target):
        return ceil((abs(target[0]-pos[0])+abs(target[1]-pos[1]))/3)
    
    def max_depth(self, start):
        return 10
    
    def print_path(self, node, p):
        step = 0
        prev_node = p[node]
        if prev_node != None:
            step = self.print_path(prev_node, p)
        print(f"{step}\t{node}")
        step = step+1
        return step