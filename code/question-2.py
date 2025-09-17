from typing import Generator


def solution() -> int:
    """Returns the sum of the even-valued terms in the Fibonacci Sequence that do not exceed 4,000,000."""
    output = 0
    for x in fibonacci_sequence():
        if x > 4_000_000:
            break
        output += x
    return output


def fibonacci_sequence() -> Generator[int, None, None]:
    """Returns the even-valued terms of the Fibonacci Sequence."""
    a, b = 1, 2
    while True:
        yield b
        a, b = a + b * 2, a * 2 + b * 3


if __name__ == "__main__":
    result = solution()
    print(
        f"The sum of the even-valued terms of the Fibonacci Seqeunce that do not exceed 4,000,000 is: {result}"
    )
