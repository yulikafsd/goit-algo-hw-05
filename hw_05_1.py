def caching_fibonacci():
    # Створює кеш
    cache = {}

    def fibonacci(n):
        # Повертає 0 та 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Повертає число Фібоначчі, якщо знаходить n у словнику
        elif cache.get(n):
            return cache[n]
        # Якщо не знаходить n у словнику, розраховує число Фібоначчі та записує в словник
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

if __name__ == '__main__':
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
