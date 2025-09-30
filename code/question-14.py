from functools import cache


def solution():
    best_i = 1
    max_length = 1
    for i in range(1, 1_000_000):
        length = collatz_sequence(i)
        if length > max_length:
            max_length = length
            best_i = i
    return best_i


@cache
def collatz_sequence(x: int) -> int:
    if x == 1:
        return 1
    elif x % 2 == 0:
        return collatz_sequence(x // 2) + 1
    else:
        return collatz_sequence(3 * x + 1) + 1


if __name__ == "__main__":
    result = solution()
    print(f"{result} produces the longest chain for numbers under 1,000,000.")
