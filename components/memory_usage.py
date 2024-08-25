import time
from resource import getpagesize
from functools import wraps
import os

def get_memory_usage():
    with open('/proc/self/status') as f:
        for line in f:
            if 'VmRSS' in line:
                return int(line.split()[1])  # Memory usage in kilobytes

def memory_test(func):
    def wrapper(*args, **kwargs):
        # Memory usage before the function runs
        mem_before = get_memory_usage()
        print("Page usage :", getpagesize())
        # Run the function
        result = func(*args, **kwargs)
        
        # Memory usage after the function runs
        mem_after = get_memory_usage()
        
        print(f"Function '{func.__name__}'")
        print(f"Memory used: {mem_after - mem_before} KB")
        
        return result

    return wrapper


# def memory_test(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        
#         result = func(*args, **kwargs)
        
#         end_time = time.time()
#         end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

#         print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
#         print(f"Memory usage: {end_mem - start_mem} KB")
        
#         return result

#     return wrapper

# Example usage
@memory_test
def example_function():
    # Example computation to test
    return sum([i * i for i in range(1000000)])
if __name__ == "__main__":
    # Running the example function
    example_function()
