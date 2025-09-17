def solution() -> int:
    """Returns the 10,001st prime number."""
    primes = []
    candidate = 3
    for _ in range(1, 10_001):
        while not is_prime(candidate, primes):
            candidate += 2
        primes.append(candidate)
        candidate += 2
    return primes[-1]


def is_prime(x: int, primes: list[int]) -> bool:
    """Returns whether x is a prime."""
    for p in primes:
        if x % p == 0:
            return False
    return True


if __name__ == "__main__":
    result = solution()
    print(f"The 10,001st prime is {result}")
