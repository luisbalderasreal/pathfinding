import state
from fibonacci_heap import FibonacciHeap

# Nodes (States) already checked.
# key: state identifier
# value: 1
checked = {}

# Heap for next node to check.
# key: d(v) + h(v)
# value: state
heap = FibonacciHeap()

# stores the fibonacci heap nodes
# key: state identifier
# value: node in FibonacciHeap
heap_nodes = {}

# Stores the distances
# key: state identifier
# value: distance from start state
d = {}

# Stores the previous vertex
# key: state identifier
# value: state
p = {}


state = PuzzleState([8,3,7,6,0,2,1,5,4])
heap_nodes[state.identifier()] = heap.insert(0, state)
d[state.identifier()] = 0
p[state.identifier()] = None

def newNode(state, next_state):
    d[next_state.identifier()] = d[state.identifier()]+1
    p[next_state.identifier()] = state
    heap_nodes[next_state.identifier()] = heap.insert(d[next_state.identifier()]+next_state.dist(), next_state)

def editNode(state, next_state):
    d[next_state.identifier()] = d[state.identifier()]+1
    p[next_state.identifier()] = state
    heap.decrease_key(heap_nodes[next_state.identifier()], d[next_state.identifier()]+next_state.dist())

while True:
    state = heap.extract_min().value
    state_id = state.identifier()
    if state_id == '123456780':
        break
    del heap_nodes[state_id]
    checked[state_id] = 1
    for next_state in state.neighbors():
        next_state_id = next_state.identifier()
        if next_state_id not in checked:
            if next_state_id not in d:
                newNode(state, next_state)
            elif d[next_state_id] > d[state_id]+1:
                editNode(state, next_state)

n = '123456780'
print(n)
while p[n] != None:
    temp = p[n].identifier()
    print(temp)
    n = temp