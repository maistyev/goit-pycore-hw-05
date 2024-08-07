def caching_fibonacci():
    '''Returns a function that calculates the n-th Fibonacci number.'''
    cache = {} # A dictionary to store the calculated Fibonacci numbers.

    def fibonacci(n: int) -> int:
        '''Calculates the n-th Fibonacci number.'''
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        result = fibonacci(n - 1) + fibonacci(n - 2) # Recursive call to calculate the n-th Fibonacci number.
        cache[n] = result # Store the result in the cache.

        return result
    
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))