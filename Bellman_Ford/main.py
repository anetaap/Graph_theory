file_path = "tests"


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = []

    def add_edges(self, start, end, weight):
        self.graph.append([start, end, weight])

    def bellman_ford(self, start_node):

        '''
        1. we set all node distances to be infinite
        2. distance from start_node is equal to 0
        3. finding the shortest path
        4. detect negative cycle
        return: the shortest path from a given node to the starting node
        '''

        distance = [float("Inf")] * self.nodes
        distance[start_node] = 0
        for i in range(self.nodes - 1):
            for start, end, weight in self.graph:
                if distance[start] != float("Inf") and distance[start] + weight < distance[end]:
                    distance[end] = distance[start] + weight

        for start, end, weight in self.graph:
            if distance[start] != float("Inf") and distance[start] + weight < distance[end]:
                print("A negative cycle has been detected.")
                return

        self.print_solution(distance)

    def print_solution(self, distance):
        print("The distance of the node from the starting node:")
        for i in range(self.nodes):
            print("{0}\t=\t{1}".format(i, distance[i]))


if __name__ == '__main__':

    file = open(file_path + "/graph.txt", 'r')
    E = int(file.readline())    # number of edges

    nodes_weights_tab = []
    for line in file:
        nodes_weights = line.rstrip().split()
        nodes_weights_tab.append(nodes_weights)

# graph creating
    graph = Graph(E)

    for edge in nodes_weights_tab:
        start = int(edge[0])
        end = int(edge[1])
        weight = int(edge[2])
        graph.add_edges(start, end, weight)

    graph.bellman_ford(0)
    file.close()
