def multiply(a: int | str, b: int | str) -> int | str:
    if isinstance(a, str) and isinstance(b, str):
        return 'One of the inputs must be number'
    else:
        return a * b
    
    


print(multiply('k', 'f')) 