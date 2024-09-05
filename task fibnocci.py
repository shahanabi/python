def fibonacci(n):
    if n<= 0:
        raise ValueError("input should be a positive integers")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(10))
