def solution() -> int:
    """Returns the sum of the multiples of 3 or 5 that are less than 1000."""
    upper_limit = 999
    return (
        sum_of_first_n_multiples(3, upper_limit // 3)
        + sum_of_first_n_multiples(5, upper_limit // 5)
        - sum_of_first_n_multiples(15, upper_limit // 15)
    )


def sum_of_first_n(n: int) -> int:
    """Returns the sum of 1 to n inclusive of n."""
    return n * (n + 1) // 2


def sum_of_first_n_multiples(k: int, n: int) -> int:
    """Returns the sum of the first n multiples of k."""
    return k * sum_of_first_n(n)


if __name__ == "__main__":
    answer = solution()
    print(f"The sum of all multiples of 3 or 5 below 1000 is {answer}")
