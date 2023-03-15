import time
def estimated_time(nb_file):   # entrer le numéro du fichier
    assert nb_file in [i for i in range(1,11)]  # on vérifie qu'il est bien entre 1 et 10
    name_route_file = "input/routes." + str(nb_file) + ".in"
    f=open(name_route_file, 'r')
    ligne1 = f.readline().split()
    n = int(ligne1[0])
    sum = 0
    p1 = "input/network."
    p2 = ".in"
    for i in range(4):  # on estime le temps avec les 10 premières lignes du fichier
        ligne = f.readline().split()
        node1 = int(ligne[0])
        node2 = int(ligne[1])
        t_dep = time.perf_counter()
        name_network_file = p1+str(nb_file)+p2
        res = graph_from_file(name_network_file).min_power(node1, node2)
        t_fin = time.perf_counter()
        sum = sum + t_fin - t_dep
    return (n * sum/4)