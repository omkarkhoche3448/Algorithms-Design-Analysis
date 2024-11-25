class Bellman_Ford:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w]) #strat vertex,end vertex,weight
    
    def Bellman(self, src):
        dist = [10000]*self.vertices #distance array  to store the shortest distance from the source vertex src to each vertex.Initially set to a large value (10000 in this case).
        dist[src] = 0 #source vertex
        
        # This part performs the edge relaxation for all the edges V-1 times,
        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                # if the current distance to u is not infinity and the distance to v through u is shorter than the current distance to v, update the distance to v.
                if dist[u] != 10000 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        for u, v, w in self.graph:  #After completing the relaxation, the algorithm checks for negative weight cycles.if it still relax es any edge, then there is a negative weight cycle.
            if dist[u] != 10000 and dist[u] + w < dist[v]:
                print("Graph contains Negative Weight Cycle!")
                
        self.printArr(dist)
    
    def printArr(self, dist):
        print("Weights according to all edges:- ")
        for i in range(self.vertices):
            print(f"{i} :- {dist[i]}")

if __name__ == "__main__":
    vertices = int(input("Enter number of vertices/nodes in the Graph :- "))
    edges = int(input("How many edges does the graph consists :- "))
    print("Enter edge in the (Start End Weight) format :- ")
    g = Bellman_Ford(vertices)
    
    for i in range(edges):
        a, b, w = input().split(" ")
        g.add_edge(int(a), int(b), int(w))
    
    g.Bellman(0)


# time complexity is O(V * E), where V is the number of vertices and E is the number of edges. 
# Dijkstra's algorithm works only with non-negative weights and uses a greedy approach.
#  The Bellman-Ford algorithm can handle negative weight edges and also detects negative weight cycles.
# After performing V-1 relaxations, the algorithm checks all edges again. If any edge can still be relaxed, it indicates the presence of a negative weight cycle.


# Enter number of vertices/nodes in the Graph :- 4
# How many edges does the graph consists :- 5
# Enter edge in the (Start End Weight) format :- 
# 0 1 1
# 1 2 -1
# 2 3 -1
# 3 1 -1
# 0 3 10
# Graph contains Negative Weight Cycle!

# "relaxation" in Bellman-Ford algorithm means trying to update the shortest distance to a vertex 
# Example:
# Suppose the current known shortest distance to vertex B is 10.
# There's an edge from A to B with weight 5, and you know the shortest distance to A is 3.
# So, the distance to B through A is 3 + 5 = 8, which is shorter than 10.