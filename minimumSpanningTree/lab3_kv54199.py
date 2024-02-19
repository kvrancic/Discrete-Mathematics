import math
import networkx as nx

def weight(i, j, a, b, c):
  return math.floor(abs(a * i - b * j) / abs(c))

n = int(input("Unesite prirodan broj n: "))
a = int(input("Unesite prirodan broj a: "))
b = int(input("Unesite prirodan broj b: "))
c = int(input("Unesite prirodan broj c: "))

G = nx.Graph()
for i in range(0, n): # 0 do n-1 jer tako trazi networkx
  G.add_node(i) 

for i in range(1, n+1):
  for j in range(i+1, n+1):
    if weight(i, j, a, b, c) != 0:
      G.add_edge(i-1, j-1, weight=weight(i, j, a, b, c)) # -1 jer se u zadatku indeksira od 1 do n, a networkx trazi 0 do n-1

if nx.is_connected(G):
  print("Graf G je povezan graf")
  tree = nx.minimum_spanning_tree(G)
  prufer = [x+1 for x in nx.to_prufer_sequence(tree)] #ovu liniju moram imati da bi povećao indekse za 1 da budu u skladu s zadatkom 
  print("Pruferov kod minimalnog razapinjuceg stabla:", prufer)
else:
  print("Graf G nije povezan graf")
