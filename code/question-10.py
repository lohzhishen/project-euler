def solution() -> int:
    """Returns the sum of all primes below 2,000,000."""
    prime_sum = 0
    upper_limit = 2_000_000
    sift = [True] * upper_limit
    for i in range(2, upper_limit):
        if sift[i]:
            prime_sum += i
            for j in range(i * i, upper_limit, i):
                sift[j] = False
    return prime_sum


if __name__ == "__main__":
    result = solution()
    print(f"The sum of all primes below 2,000,000 is {result}")
