# sample_script_with_ipdb.py

import ipdb

def buggy_function(a, b):
    result = a + b
    return result

def main():
    x = 5
    y = "10"  # This should be an integer, but it's a string
    print("Before calling buggy_function")
    
    print(dir(ipdb))
    # Set a breakpoint here
    ipdb.set_trace()
    
    # ipdb.launch_ipdb_on_exception(ipdb.set_trace())
    result = buggy_function(x, y)
    print("After calling buggy_function")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
