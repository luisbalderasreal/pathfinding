from random import shuffle

class Puzzle3x3:
    
    default_target = '123456780'
    
    #123
    #456
    #780
    distanceDict = {
        1: [0,1,2,1,2,3,2,3,4],
        2: [1,0,1,2,1,2,3,2,3],
        3: [2,1,0,3,2,1,4,3,2],
        4: [1,2,3,0,1,2,1,2,3],
        5: [2,1,2,1,0,1,2,1,2],
        6: [3,2,1,2,1,0,3,2,1],
        7: [2,3,4,1,2,3,0,1,2],
        8: [3,2,3,2,1,2,1,0,1],
        0: [4,3,2,3,2,1,2,1,0]
    }
    
    @classmethod
    def random_start(cls):
        seq = [0,1,2,3,4,5,6,7,8]
        shuffle(seq)
        
        inversions = 0
        checklist = [False for i in range(9)]
        for index in range(9):
            if checklist[index] == False:
                checklist[index] = True
                destination = seq[index]
                while destination != index:
                    inversions = inversions + 1
                    checklist[destination] = True
                    destination = seq[destination]
        
        zero_dist = cls.distanceDict[0][seq.index(8)]
        
        if (inversions + zero_dist)%2 == 1:
            ind_1 = seq.index(0)
            ind_2 = seq.index(1)
            seq[ind_1] = 1
            seq[ind_2] = 0
        
        return ''.join(list(map(lambda x: str((x+1)%9), seq)))

    @classmethod
    def neighbors(cls, seq):
        emptyIndex = seq.index('0')
        charList = list(seq)
        neighborIndexList = []
        neighborList = []
        if emptyIndex > 2:
            neighborIndexList.append(emptyIndex-3)
        if emptyIndex < 6:
            neighborIndexList.append(emptyIndex+3)
        if emptyIndex%3 != 0:
            neighborIndexList.append(emptyIndex-1)
        if emptyIndex%3 != 2:
            neighborIndexList.append(emptyIndex+1)
        for i in neighborIndexList:
            newSeq = charList.copy()
            newSeq[i], newSeq[emptyIndex] = '0', newSeq[i]
            newSeq = ''.join(newSeq)
            neighborList.append((newSeq, 1))
        return neighborList
    
    @classmethod
    def heuristic(cls, seq, target_seq):
        h = 0
        for n in range(1,9):
            h += cls.distanceDict[n][seq.index(str(n))]
        return h
    
    @classmethod
    def max_depth(cls, start):
        return 181440
    
    @classmethod
    def print_path(cls, node, p):
        step = 0
        prev_node = p[node]
        if prev_node != None:
            step = cls.print_path(prev_node, p)
        print(f"{step}\t{node}")
        step = step+1
        return step