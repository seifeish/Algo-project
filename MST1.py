import heapq

def prims_algorithm(graph):

    if not graph:
        return []  
    
    start_node = list(graph.keys())[0]  
    visited = set([start_node])  
    min_heap = []  
    mst = []  
    
    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))
    

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)  
        
        if v not in visited:  
            visited.add(v)  
            mst.append((u, v, weight))  
            
            for neighbor, edge_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, v, neighbor))
    
    return mst


def analyze_prims_algorithm():
    
    return 


if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)]
    }

    mst_result = prims_algorithm(graph)
    print("Minimum Spanning Tree:", mst_result)

    analysis_result = analyze_prims_algorithm()
    print("\nAnalysis of Prim's Algorithm:\n", analysis_result)

