from queue import Queue

R, C = map(int, input().split(''))
n_boom = int(input())

V = None
E = None
visited = [False for i in range(R)]
path = [0 for i in range(R)]
graph = [[] for i in range(R)]
for i in range(n_boom):
    line, num, *positions = map(int, input().split(' '))
    for j in positions:
        graph[i][positions] = 0


def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    q = Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u


def print_path(s, f):
    b = []
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print('NO')
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    for i in range(len(b) - 1, -1, -1):
        print(b[i], end=' ')
