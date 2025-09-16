def solution() -> int:
    """Returns the largest prime factor of 600,851,475,143."""
    # x is not even so 2 is definitely not a prime factor
    x = 600_851_475_143
    for i in range(3, x + 1, 2):
        while x % i == 0:
            x = x // i
        if x == 1:
            return i


if __name__ == "__main__":
    result = solution()
    print(f"The largest prime factor of 600,851,475,143 is {result}")
