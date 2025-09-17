from functools import reduce


def solution() -> int:
    """Returns the smallest positive number that is evenly divisible by all numbers from 1 to 20."""
    return reduce(lcm, range(2, 21), 1)


def lcm(x: int, y: int) -> int:
    """Returns the lowest common multiple between x and y."""
    return x * y // gcd(x, y)


def gcd(x: int, y: int) -> int:
    """Returns the greatest common divisor between x and y."""
    if x > y:
        return gcd(y, x)
    while y != 0:
        x, y = y, x % y
    return x


if __name__ == "__main__":
    result = solution()
    print(
        f"The smallest positive number that is evenly divisible by all numbers from 1 to 20 is {result}"
    )
