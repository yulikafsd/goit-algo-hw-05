def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif cache.get(n):
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

if __name__ == '__main__':
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
