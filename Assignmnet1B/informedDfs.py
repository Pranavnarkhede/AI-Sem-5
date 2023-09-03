def build_graph():
    graph = {}
    
    num_nodes = int(input("Enter the number of nodes: "))
    
    for i in range(num_nodes):
        node = input("Enter a node: ")
        num_edges = int(input("Enter the number of edges attached to node {node}: "))
        edge_list = []
        
        for j in range(num_edges):
            edge = input(f"Enter an edge attached to node {node}: ")
            edge_list.append(edge)
        
        graph[node] = edge_list
    
    return graph

visited = set()

def dfs(visited, graph, node, key):
    if node == key:
        print(node)
        return True
    
    print(node)
    visited.add(node)
       
    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(visited, graph, neighbour, key):
                return True

graph = build_graph()
key = input("Enter Final Node: ")
print("Following is DFS:")
dfs(visited, graph, 'A', key)

# Output
# Enter the number of nodes: 4
# Enter a node: A
# Enter the number of edges attached to node A: 2
# Enter an edge attached to node A: B
# Enter an edge attached to node A: C
# Enter a node: B
# Enter the number of edges attached to node B: 1
# Enter an edge attached to node B: D
# Enter a node: C
# Enter the number of edges attached to node C: 0
# Enter a node: D
# Enter the number of edges attached to node D: 0
# Enter Final Node: B
# Following is DFS:
# A
# B


