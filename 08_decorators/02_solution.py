from _01_solution import timer



def debug(func):
    def wrapper(*args, **kwargs):
        arg_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f"{k} = {v}" for k,v in kwargs.items())
        print(f"Calling {func.__name__}({arg_values}, {kwargs_values})")
        return func(*args, **kwargs)
    return wrapper



@debug
@timer
def greet(greeting = "Hello", name = "World"):
    print(f"{greeting}, {name}!")

greet("Hi",name = "Alice")