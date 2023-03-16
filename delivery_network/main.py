from graph import Graph, graph_from_file

data_path = "input/"
file_name = "network.5.in"

g = graph_from_file(data_path + file_name)

# print(g)

h = g.kruskal()

print(h.min_power(1, 35874))
print(h.min_power(1, 35774))
print(h.min_power(1, 35674))
print(h.min_power(1, 35214))
print(h.min_power(1, 35894))
print(h.min_power(1, 3587))
print(h.min_power(1, 35832))
print(h.min_power(1, 35814))
print(h.min_power(1, 15874))
print(h.min_power(1, 97874))
print(h.min_power(1, 46874))
print(h.min_power(1, 78874))
