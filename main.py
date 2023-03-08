import heapq

def dijkstra(graph, start):
  distances = {v: float('inf') for v in graph}
  distances[start] = 0

  pq = [(0, start)]

  while pq:
    current_distance, current_vertex = heapq.heappop(pq)

    if current_distance > distances[current_vertex]:
        continue

    for neighbor, weight in graph[current_vertex].items():
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))

  return distances

graph = {
  'A': {'B': 3, 'C': 1},
  'B': {'A': 3, 'C': 7, 'D': 5},
  'C': {'A': 1, 'B': 7, 'D': 2},
  'D': {'B': 5, 'C': 2}
}

start = 'A'

distances = dijkstra(graph, start)

print(distances)