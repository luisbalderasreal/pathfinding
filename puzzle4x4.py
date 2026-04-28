from random import choice

class Puzzle4x4:
    
    # A=10, B=11, C=12, D=13, E=14, F=15
    default_target = '123456789ABCDEF0'

    distanceDict = {
        1: [0,1,2,3, 1,2,3,4, 2,3,4,5, 3,4,5,6],
        2: [1,0,1,2, 2,1,2,3, 3,2,3,4, 4,3,4,5],
        3: [2,1,0,1, 3,2,1,2, 4,3,2,3, 5,4,3,4],
        4: [3,2,1,0, 4,3,2,1, 5,4,3,2, 6,5,4,3],
        5: [1,2,3,4, 0,1,2,3, 1,2,3,4, 2,3,4,5],
        6: [2,1,2,3, 1,0,1,2, 2,1,2,3, 3,2,3,4],
        7: [3,2,1,2, 2,1,0,1, 3,2,1,2, 4,3,2,3],
        8: [4,3,2,1, 3,2,1,0, 4,3,2,1, 5,4,3,2],
        9: [2,3,4,5, 1,2,3,4, 0,1,2,3, 1,2,3,4],
        10: [3,2,3,4, 2,1,2,3, 1,0,1,2, 2,1,2,3],
        11: [4,3,2,3, 3,2,1,2, 2,1,0,1, 3,2,1,2],
        12: [5,4,3,2, 4,3,2,1, 3,2,1,0, 4,3,2,1],
        13: [3,4,5,6, 2,3,4,5, 1,2,3,4, 0,1,2,3],
        14: [4,3,4,5, 3,2,3,4, 2,1,2,3, 1,0,1,2],
        15: [5,4,3,4, 4,3,2,3, 3,2,1,2, 2,1,0,1],
        0: [6,5,4,3, 5,4,3,2, 4,3,2,1, 3,2,1,0]
    }
    
    @classmethod
    def random_start(cls):
        seq = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','0']
        previous_seq = None
        for i in range(30):
            emptyIndex = seq.index('0')
            neighborIndexList = []
            neighborList = []
            if emptyIndex > 3:
                neighborIndexList.append(emptyIndex-4)
            if emptyIndex < 12:
                neighborIndexList.append(emptyIndex+4)
            if emptyIndex%4 != 0:
                neighborIndexList.append(emptyIndex-1)
            if emptyIndex%4 != 3:
                neighborIndexList.append(emptyIndex+1)
            for i in neighborIndexList:
                newSeq = seq.copy()
                newSeq[i], newSeq[emptyIndex] = '0', newSeq[i]
                if newSeq != previous_seq:
                    neighborList.append(newSeq)
            previous_seq = seq
            seq = choice(neighborList)
        seq = ''.join(seq)
        return seq
    
    @classmethod
    def neighbors(cls, seq):
        emptyIndex = seq.index('0')
        charList = list(seq)
        neighborIndexList = []
        neighborList = []
        if emptyIndex > 3:
            neighborIndexList.append(emptyIndex-4)
        if emptyIndex < 12:
            neighborIndexList.append(emptyIndex+4)
        if emptyIndex%4 != 0:
            neighborIndexList.append(emptyIndex-1)
        if emptyIndex%4 != 3:
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
        for i in range(1,16):
            match i:
                case 10:
                    n = 'A'
                case 11:
                    n = 'B'
                case 12:
                    n = 'C'
                case 13:
                    n = 'D'
                case 14:
                    n = 'E'
                case 15:
                    n = 'F'
                case _:
                    n = str(i)
            h += cls.distanceDict[i][seq.index(n)]
        return h
    
    @classmethod
    def max_depth(cls, start):
        return 50
    
    @classmethod
    def print_path(cls, node, p):
        step = 0
        prev_node = p[node]
        if prev_node != None:
            step = cls.print_path(prev_node, p)
        print(f"{step}\t{node}")
        step = step+1
        return step