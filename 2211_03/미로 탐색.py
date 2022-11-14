# https://www.acmicpc.net/problem/2178
import sys, collections
N, M = map(int, sys.stdin.readline().split())
MAZE = [list(sys.stdin.readline().strip()) for _ in range(N)]

q = collections.deque()
q.append((0, 0))
visited = [[1e9] * M for _ in range(N)]
visited[0][0] = 1
while q:
    r, c = q.popleft()
    move = visited[r][c] + 1
    for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + nr, c + nc
        if 0 <= nr < N and 0 <= nc < M and MAZE[nr][nc] == '1' and visited[nr][nc] > move:
            q.append((nr, nc))
            visited[nr][nc] = move

print(visited[N-1][M-1])
