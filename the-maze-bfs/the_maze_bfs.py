from collections import deque


class Solution:
    def hasPath(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> bool:
        rows, cols = len(maze), len(maze[0])
        visited = set()

        queue = deque([tuple(start)])
        visited.add(tuple(start))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            current_row, current_col = queue.popleft()

            if [current_row, current_col] == destination:
                return True

            for dr, dc in directions:
                row, col = current_row + dr, current_col + dc

                while 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0:
                    row += dr
                    col += dc

                newRow, newCol = row - dr, col - dc

                if (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))

        return False


def main():
    # Test data
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    start = [0, 4]
    destination = [4, 4]

    solution = Solution()

    print(solution.hasPath(maze, start, destination))


if __name__ == "__main__":
    main()
