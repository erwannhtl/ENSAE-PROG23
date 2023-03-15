from graph import Graph, UnionFind, graph_from_file, kruskal

data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(g)

f=kruskal(data_path + file_name)
print(f)