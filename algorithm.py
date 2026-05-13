import heapq

def dijkstra(graph, start, goal):

    queue = [(0, start, [])]

    visited = set()

    while queue:

        cost, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        path = path + [current]

        if current == goal:
            return cost, path

        for neighbor, weight in graph[current].items():

            if neighbor not in visited:

                heapq.heappush(
                    queue,
                    (cost + weight, neighbor, path)
                )

    return float("inf"), []