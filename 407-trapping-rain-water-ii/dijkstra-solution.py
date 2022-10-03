import itertools
import functools
from collections import defaultdict
from collections import namedtuple
from heapq import heappush
from heapq import heappop

DEST = 0
COST = 1

Edge = namedtuple('Edge', ['target', 'cost'])
PrioqItem = namedtuple('PrioqItem', ['dist', 'node'])


def get_id(i, j, m):
    return i * m + j


def dijkstra(graph, n, source_node):
    dist = [(1 << 31) - 1] * n
    dist[source_node] = 0

    seen = set()
    prioq = [PrioqItem(dist=0, node=source_node)]
    while prioq != []:
        item = heappop(prioq)
        seen.add(item.node)
        for edge in graph[item.node]:
            if dist[edge.target] > max(edge.cost, item.dist):
                dist[edge.target] = max(edge.cost, item.dist)
                if edge.target not in seen:
                    heappush(prioq, PrioqItem(
                        dist=dist[edge.target], node=edge.target))
    return dist


class Solution:
    def trapRainWater(self, height_map):
        if not height_map or not height_map[0]:
            return 0

        n = len(height_map)
        m = len(height_map[0])
        source_node = n * m

        id = functools.partial(get_id, m=m)

        graph = defaultdict(list)
        for i, j in itertools.product(range(n), range(m)):
            for n_i, n_j in {(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)}:
                if n_i < 0 or n_i >= n or n_j < 0 or n_j >= m:
                    continue
                graph[id(n_i, n_j)].append(
                    Edge(id(i, j), height_map[n_i][n_j]))
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                graph[source_node].append(Edge(id(i, j), 0))

        print(graph)

        dist = dijkstra(graph, n * m + 1, source_node)
        ans = sum(
            max(dist[id(i, j)] - height_map[i][j], 0)
            for i, j in itertools.product(range(n), range(m))
        )
        return ans


assert Solution().trapRainWater(
    [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]) == 4
assert Solution().trapRainWater([
    [2, 3, 2],
    [2, 1, 2],
    [2, 2, 2],
]) == 1
