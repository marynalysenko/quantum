# TASK 1:
# You have a matrix MxN that represents a map.
# There are 2 possible states on the map: 1 - islands, 0 - the ocean.
# Your task is to calculate the number of islands in the most effective way.


def numIslands(grid: list[list[int]]) -> int:
    """
    Counts the number of islands in a given grid. An island is defined as a group of adjacent lands 1,
    connected horizontally or vertically. The function uses depth-first search (DFS) to traverse through the grid.

    Parameters:
    grid (List[List[int]]): A 2D grid map of 1 (land) and 0 (water).

    Returns:
    int: The total number of islands found in the grid.
    """
    # Check if the grid is empty
    if not grid:
        return 0

    def dfs(i, j):
        """
        Depth-first search to mark all adjacent lands of an island as visited.

        Parameters:
        i (int): The row index in the grid.
        j (int): The column index in the grid.
        """
        # Check for invalid indices and water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return

        # Mark the land as visited
        grid[i][j] = 0

        # Explore the adjacent lands (up, down, left, right)
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If land is found, explore the island and increment the count
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1

    return count


def main():
    # Test cases
    grid1 = [[0, 1, 0], [0, 0, 0], [0, 1, 1]]

    grid2 = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]

    grid3 = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]]

    print("Island count for grid 1:", numIslands(grid1))
    print("Island count for grid 2:", numIslands(grid2))
    print("Island count for grid 3:", numIslands(grid3))


if __name__ == "__main__":
    main()