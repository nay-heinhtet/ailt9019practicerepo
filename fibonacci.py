def first_n_fibonacci(n):
    fibs = []
    a, b = 0, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs


if __name__ == "__main__":
    for num in first_n_fibonacci(5):
        print(num)
