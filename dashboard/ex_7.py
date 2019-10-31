
def cache(fn):
    fn._cache = {}
    def wrapper(*args, **kwargs):
        if not args in fn._cache:
            fn._cache[args] = fn(*args, **kwargs)
        return fn._cache[args]
    return wrapper

@cache
def fib(n):
    if n < 1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(1000):
    print(f'{i} -> {fib(i)}')

