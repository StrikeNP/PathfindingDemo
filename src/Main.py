import time

from Search import Search
from src.Graph import Graph

if __name__ == "__main__":
    print("Generating new graph")
    graph = Graph(max_x=20, max_y=20, node_chance=25, adj_chance=30, nearby_threshold=3)
    print("Saving graph to img")
    graph.save('graphQuestion')
    searcher = Search(graph, 10)
    startime = time.time_ns()
    solution = searcher.find_path()
    runtime = time.time_ns() - startime
    graph.solution = solution
    graph.save('graphAnswer')
    print('Solution length: ' + str(len(solution)) + ' found in ' + str(runtime))
    # print(solution)
    # for element in solution:
    #     print("x " + str(element.x_pos) + " Y " + str(element.y_pos) + "\n")