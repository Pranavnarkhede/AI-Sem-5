def build_graph():
    graph = {}
    
    nodes = int(input("Enter the number of nodes: "))
    
    for i in range(nodes):
        node = input("Enter a node: ")
        edges = int(input("Enter the number of edges attached to node {node}: "))
        edge_list = []
        
        for j in range(edges):
            edge = input(f"Enter an edge attached to node {node}: ")
            edge_list.append(edge)
        
        graph[node] = edge_list
    
    return graph

def bfs(graph, start, key):
    queue = []
    queue.append(start)
    visited = set()
    
    while queue:
        node = queue.pop(0)
        print(node)
        
        if node == key:
            print("Key node found!")
            return True
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    
    print("Key node not found.")
    return False

graph = build_graph()
start_node = input("Enter the starting node: ")
key_node = input("Enter the target node to find (BFS): ")

print("Breadth-First Search:")
bfs(graph, start_node, key_node)


Enter the number of nodes: 4
Enter a node: A
Enter the number of edges attached to node {node}: 2
Enter an edge attached to node A: B
Enter an edge attached to node A: C
Enter a node: B
Enter the number of edges attached to node {node}: 1
Enter an edge attached to node B: D
Enter a node: C
Enter the number of edges attached to node {node}: 0
Enter a node: D
Enter the number of edges attached to node {node}: 0
Enter the starting node: A
Enter the target node to find (BFS): C
Breadth-First Search:
A
B
C
Key node found!
> 
