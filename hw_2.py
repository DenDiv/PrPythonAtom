def dec_counter(f):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return f(*args, **kwargs)
    wrapper.count = 0
    return wrapper
@dec_counter
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(35))
print(fib.count)
