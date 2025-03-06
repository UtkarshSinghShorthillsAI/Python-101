import time

def cache(func):
    cache_val = {}
    print("Cache value:", cache_val)
    def wrapper(*args):
        if args in cache_val:
            return cache_val[args]
        result = func(*args)
        cache_val[args] = result
        return result
    return wrapper

@cache
def long_running_fnc(a, b):
    print("Starting long running function")
    time.sleep(4)
    return f"Done {a} + {b} = {a + b}"


print(long_running_fnc(1, 2))
print(long_running_fnc(1, 2))