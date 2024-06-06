# -*- coding: utf-8 -*-
"""shortestpath.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JGeKIrmvvFNi11hEYmK-ADVTVlhT9vAZ
"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Step 2.1: Create a queue for BFS and add the start node to it
    queue = deque([[start]])
    # Step 2.2: Create a set to keep track of the visited nodes
    visited = set()

    # Step 2.3: Loop until the queue is empty
    while queue:
        # Step 2.4: Get the first path from the queue
        path = queue.popleft()
        # Step 2.5: Get the last node from the path
        node = path[-1]

        # Step 2.6: Check if the node is the goal
        if node == goal:
            return path

        # Step 2.7: If not, mark the node as visited
        if node not in visited:
            visited.add(node)
            # Step 2.8: Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                print(f"Enqueued new path: {new_path}")

    return None

# Example Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

start_node = 'A'
goal_node = 'E'
shortest_path = bfs_shortest_path(graph, start_node, goal_node)
print(f"The shortest path from {start_node} to {goal_node} is: {shortest_path}")