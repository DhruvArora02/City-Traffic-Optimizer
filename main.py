from ford_fulkerson import ford_fulkerson
from utils import read_graph_from_file

def main():
    input_file = "input_example.txt"
    graph, n = read_graph_from_file(input_file)
    source, sink = 1, n
    max_flow = ford_fulkerson(graph, source, sink)
    print(f"Maximum Traffic Flow: {max_flow}")

if __name__ == "__main__":
    main()
