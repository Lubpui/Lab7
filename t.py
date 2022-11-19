# graph = {'A': ['B', 'C', 'G'],
#          'B': ['A','E'],
#          'C': ['A', 'D'],
#          'D': ['C','H'],
#          'E': ['B','G'],
#          'F': ['C','D','G'],
#          'G': ['A','E','F'],
#          'H': ['D','F']}

graph = {'A': ['B','D','E'],
         'B': ['A','C','E'],
         'C': ['B','E','F','G'],
         'D': ['A','E'],
         'E': ['B','F','D','A','C'],
         'F': ['C','E','G'],
         'G': ['C','F']}

visited = []

def dfs_traversal(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited


def bfs_traversal(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


bfs_path = bfs_traversal(graph, 'A')  # returns ['A', 'B', 'E', 'C', 'D', 'F', 'G']
print(bfs_path)

dfs_path = dfs_traversal(graph,'A')
print(dfs_path)