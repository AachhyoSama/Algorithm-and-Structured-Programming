
class Solution:
    def hasPath(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> bool:
        def dfs(x: int, y: int) -> bool:
            if [x, y] == destination:
                return True

            visited.add((x, y))

            for dx, dy in directions:
                new_x, new_y = x, y
                while (
                    0 <= new_x + dx < m
                    and 0 <= new_y + dy < n
                    and maze[new_x + dx][new_y + dy] == 0
                ):
                    new_x += dx
                    new_y += dy

                if (new_x, new_y) not in visited and dfs(new_x, new_y):
                    return True

            return False

        m, n = len(maze), len(maze[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        return dfs(start[0], start[1])
