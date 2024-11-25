V = 4
# Goal
# Assign colors to the vertices of the graph such that:

# No two adjacent vertices have the same color.
# Use at most M colors.

def print_solution(color):
    print("Solution Exists: Following are the assigned colors")
    print(" ".join(map(str, color)))

def is_safe(v, graph, color, c):
    # Check if the color 'c' is safe for the vertex 'v'
    for i in range(V):
        if graph[v][i] and c == color[i]:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    # Base case: If all vertices are assigned a color, return true
    if v == V:
        return True

#Loop through all possible colors (1 to M) and try assigning each to the current vertex v.
    for c in range(1, m + 1):
        # Check if assignment of color 'c' to 'v' is fine
        #  doesn’t conflict with adjacent vertices.
        if is_safe(v, graph, color, c):
            color[v] = c

            # Recur to assign colors to the rest of the vertices
            # After assigning a color, move to the next vertex (v + 1) recursively.
            if graph_coloring_util(graph, m, color, v + 1):
                return True

            # If assigning color 'c' doesn't lead to a solution, remove it
            # If the recursive call fails (no valid coloring possible), we "unassign" the color (color[v] = 0) and try the next color.
            color[v] = 0

    # If no color can be assigned to this vertex, return false
    return False

def graph_coloring(graph, m):
    color = [0] * V

    # Call graph_coloring_util() for vertex 0
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False

    # Print the solution
    print_solution(color)
    return True

# Driver code
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]

    m = 3

    # Function call
    graph_coloring(graph, m)
    
# Solution Exists: Following are the assigned colors
# 1 2 3 2



# Backtracking is a technique where we:
# Try a possible solution. If it works, continue.If it fails, revert 

# How Backtracking Works Here:

# Start with vertex 0 and try all colors (1 to M).
# Assign a color that doesn’t conflict with adjacent vertices.
# Move to the next vertex and repeat.
# If a vertex cannot be assigned any valid color, undo the color assignment for the previous vertex and try a different color for it.
# The worst-case complexity is O(M^V), where M is the number of colors and V is the number of vertices...