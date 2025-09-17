def solution() -> int:
    """Returns the value of abc such that a^2 + b^2 = c^2 and a + b + c == 1000."""
    squares = [1, 4]
    for c in range(3, 1_000):
        result = pythagorean_triplet(c, squares, 1_000)
        if result:
            return result[0] * result[1] * result[2]
        squares.append(c**2)
    return -1


def pythagorean_triplet(
    c: int, squares: list[int], s: int
) -> tuple[int, int, int] | None:
    """Returns a, b, c such that a^2 + b^2 = c^2 and a + b + c == s if it exists."""
    i, j, c2 = 0, len(squares) - 1, c**2
    while i <= j:
        c2_hat = squares[i] + squares[j]
        if c2 == c2_hat:
            if i + j + c + 2 == s:
                return i + 1, j + 1, c
            i += 1
            j -= 1
        elif c2 > c2_hat:
            i += 1
        else:
            j -= 1
    return None


if __name__ == "__main__":
    result = solution()
    print(f"The value of abc is {result}")
