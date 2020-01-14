n = 3
a = [i for i in range(n)]
d = [
    [0, 2, 3],
    [2, 0, 6],
    [3, 6, 0]
]
visited = [False] * n


def tsp(path, visited, cur):

    if len(visited) == n:
        if path:
            return cur + d[path[0]][path[-1]]

    ret = 100000000000000
    for i in range(n):
        if visited[i]:
            continue
        path.append(i)
        visited[i] = True
        if path:
            here = path[-1]
            cand = tsp(path, visited, cur + d[here][i])
            ret = min(ret, cand)
        visited[i] = False
        path.pop()
    return ret


print(tsp([], visited, 0))
