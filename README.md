# City-Traffic-Optimizer

__Project Overview__ -

This project focuses on optimizing traffic flow in a city's road network using the Ford-Fulkerson algorithm. The road network is modeled as a directed graph where intersections are represented as nodes, roads as edges, and each edge has a capacity indicating the maximum number of vehicles it can handle. The algorithm computes the maximum flow of traffic from a designated source (entry point) to a sink (destination).

__Key Features__ -

- Models a road network as a graph with user-defined nodes and edges.
- Calculates the maximum traffic flow from a source to a sink using the Ford-Fulkerson algorithm.
- Identifies bottlenecks in the network that limit traffic capacity.
- Accepts input through a text file for flexibility and reusability.
- Scalable to larger networks and adaptable to real-world scenarios.

__Technologies Used__ -
- **Python**: Core programming language for implementing the algorithm.
- **Collections Module**: Utilized for `defaultdict` and `deque` to manage graph structures and BFS efficiently.

__How It Works__ -
1. **Input Representation**:  
- The road network is provided as input through a text file.  
- Example format:  6 8 1 2 16 1 3 13 2 3 10 2 4 12 3 2 4 3 5 14 4 5 7 4 6 20 5 6 4
- First line: Number of nodes (`n`) and edges (`m`).
- Subsequent lines: Each edge represented by `u` (start node), `v` (end node), and `capacity`.

2. **Ford-Fulkerson Algorithm**:  
- The graph is converted into a residual graph, which tracks remaining capacities.
- Breadth-First Search (BFS) finds augmenting paths from source to sink.
- The flow along the path is updated until no more augmenting paths exist.

3. **Output**:  
- The program calculates and prints the maximum traffic flow.  
- Example Output: Maximum Traffic Flow: 23

4. **Execution**:
- Run the program after preparing an input file:
