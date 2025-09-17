def solution() -> int:
    """Return the difference between the sum of squares of 1 to 100 and the square of the sum of 1 to 100."""
    return sum((2 * i * j for i in range(1, 101) for j in range(1, i)))


if __name__ == "__main__":
    result = solution()
    print(
        f"The difference between the sum of squares of 1 to 100 and the square of the sum of 1 to 100 is {result}"
    )
