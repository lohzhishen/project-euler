from typing import Generator


def solution() -> int:
    """Return the first triangle number with more than 500 divisors."""
    for num in get_triangle_numbers():
        if count_divisors(num) > 500:
            return num


def count_divisors(x: int) -> int:
    """Returns the number of divisors of x."""
    square_root = int(x**0.5)
    counts = 1 if x % square_root == 0 else 0
    for i in range(1, square_root):
        if x % i == 0:
            counts += 2
    return counts


def get_triangle_numbers() -> Generator[int, None, None]:
    """Returns a sequence of triangle numbers."""
    s, i = 0, 1
    while True:
        s += i
        i += 1
        yield s


if __name__ == "__main__":
    result = solution()
    print(f"The first triangle number with more than 500 divisors is {result}")
