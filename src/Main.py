from Search import Search
from src.Graph import Graph

if __name__ == "__main__":
    print("Generating new graph")
    graph = Graph(max_x=10, max_y=10, node_chance=25, adj_chance=30, nearby_threshold=3)
    print("Saving graph to img")
    graph.save()
    searcher = Search(graph, 10)
    solution = searcher.find_path()
    graph.solution = solution
    graph.save()
    # print(solution)
    # for element in solution:
    #     print("x " + str(element.x_pos) + " Y " + str(element.y_pos) + "\n")