"""Solves a maze using depth-first search with a stack."""
def dfs_maze_solver(maze, start):

    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    stack = [(start[0], start[1])]
    visited[start[0]][start[1]] = True

    while stack:
        row, col = stack.pop()
        if maze[row][col] == "E":  # Found the exit
            return True

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] != "#" and not visited[new_row][
                new_col]:
                stack.append((new_row, new_col))
                visited[new_row][new_col] = True

    return False

# Example usage
maze = [
    ["S", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", "#", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
start_position = (0, 0)
print(dfs_maze_solver(maze, start_position))  # Output: True if exit is reachable, False otherwise
