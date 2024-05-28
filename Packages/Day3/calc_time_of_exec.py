import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@calculate_time
def example_function_1():
    # Your code here
    time.sleep(2)

@calculate_time
def example_function_2():
    # Your code here
    time.sleep(1)
def main():
    # Call the decorated functions
    example_function_1()
    example_function_2()
if __name__ == "__main__":
    main()