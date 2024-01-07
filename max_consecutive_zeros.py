def max_consecutive_zeros(n):
    binary_representation = bin(n)[2:]
    max_zeros = 0
    current_zeros = 0
    for digit in binary_representation:
        if digit == '0':
            current_zeros += 1
            max_zeros = max(max_zeros, current_zeros)
        else:
            current_zeros = 0
    return max_zeros
if __name__ == "__main__":
    test_cases = [22, 25, 268]
    for test_case in test_cases:
        result = max_consecutive_zeros(test_case)
        print(f"Broj {test_case} ima {result} uzastopnih nula")
