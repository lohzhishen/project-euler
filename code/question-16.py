def solution():
    x = 1000
    digits = [1]
    for _ in range(x):
        carry_over = 0
        for i in range(len(digits)):
            digits[i] = digits[i] * 2 + carry_over
            carry_over = digits[i] // 10
            digits[i] = digits[i] % 10
        if carry_over != 0:
            digits.append(carry_over)
    return sum(digits)


if __name__ == "__main__":
    result = solution()
    print(f"The sum of digits is {result}")
