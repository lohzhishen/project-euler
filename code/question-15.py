def solution():
    # in a 20x20 grid, there are 21x21 possible positions
    n = 20
    ways = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        ways[i][-1] = 1
        ways[-1][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            ways[i][j] = ways[i + 1][j] + ways[i][j + 1]
    return ways[0][0]


if __name__ == "__main__":
    result = solution()
    print(f"There are {result} paths thorugh a 20x20 grid")
