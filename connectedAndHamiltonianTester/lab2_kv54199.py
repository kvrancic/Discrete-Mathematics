import numpy as np 

def DFS(adj: np.ndarray, n: int, start: int, visited: int) -> bool:  
    visited[start] = True
    for i in range(n):
        if (adj[start][i] == 1 and (not visited[i])):
            DFS(adj, n, i, visited)

def connected(visited: int) -> bool: 
    for i in visited: 
        if(i == False):
            return False
    return True

def hamilton(n: int, adj: np.ndarray) -> bool:
    visited = np.zeros(n, dtype=int)
    length = 1
    def visit(curr: int) -> bool:
        nonlocal visited, length 
        if length == n and adj[curr][0]:
            return True
        visited[curr] = 1 
        for i, c in enumerate(adj[curr]):
            if c and not visited[i]:
                length += 1
                if visit(i):
                    return True
                length -= 1
                visited[i] = 0
        return False

    return visit(0)

n = int(input("Unesite prirodan broj: "))
k1 = int(input("Unesite vrijednost prirodnog broja k_1: "))
k2 = int(input("Unesite vrijednost prirodnog broja k_2: "))
k3 = int(input("Unesite vrijednost prirodnog broja k_3: "))
k4 = int(input("Unesite vrijednost prirodnog broja k_4: "))
matrica = np.zeros([n, n], dtype = int)

for i in range(n):
    for j in range(n):
        if(abs(i - j) == k1 or abs(i - j) == k2 or abs(i - j) == k3 or abs(i - j) == k4):
            matrica[i][j] = 1

visited = [False] * n
DFS(matrica, n, 0, visited)

x = []

if(connected(visited)): 
    print("Graf G je povezan graf")
    if(hamilton(n, matrica)): 
        print("Graf G je hamiltonski graf")
    else: 
        print("Graf G nije hamiltonski graf")
else:
    print("Graf G nije povezan")
    print("Graf G nije hamiltonski graf")