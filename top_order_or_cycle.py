import sys
sys.setrecursionlimit(10**6)

info = sys.stdin.readlines()
num_nodes = int(info[0].split()[0]) #store number of nodes
num_edges = int(info[0].split()[1]) #store number of edges
edges = info[1:] #store edge array
adjacency_list = [[] for i in range(num_nodes)] #initialize adjacency list

#construct adjacency list using edge list
for e in edges:
    e = e.split() #since edges are given as string
    origin = e[0] #node where directed edge starts
    destination = e[1] #node where directed edge ends
    adjacency_list[int(origin)].append(int(destination))
    #modify adjacency list sub-list corresponding to origin node adding destination node

used = [[] for x in range(num_nodes)] #nodes that have been visited
active = [[] for x in range(num_nodes)] #node that is in process of being visited and part of current stack
stack = [] #initialize topological order array
cycle = [] #initialize
begin_cycle = -1 #initialize tracker for beginning of cycle

def dfs(node_index):
    global begin_cycle
    used[node_index] = True #mark node as visited for good
    active[node_index] = True #upon first call the node is currently being visited
    for destination in adjacency_list[node_index]:
        if not used[destination]: #a new node
            if dfs(destination): #recursively searches for cycles on freshly discovered destination nodes
                if begin_cycle!=-1:
                    cycle.insert(0, node_index)
                if begin_cycle==node_index:
                    begin_cycle=-1
                return True
        else:
            if active[destination]: #a cycle is found when we stumble upon the node originally being examined
                begin_cycle = destination
                cycle.insert(0,node_index)
                return True
    active[node_index] = False #exiting node visitation
    stack.append(node_index) #recursive calls return reverse order of topological nodes
    return False

def has_cycle():
    for i in range(num_nodes):
        if not used[i]:
            if dfs(i):
                return True
    return False

if has_cycle():
    print('cycle')
    for node in cycle:
        print(node)
else:
    print('order')
    for node in stack[-1::-1]:
        print(node)