import random

def retry(max_retry):
    def decorator_retry(func):
        def wrapper(*args, **kwargs):
            retry_count = 0
            while retry_count < max_retry:
                result = func(*args, **kwargs)
                if result < 3:
                    print("Success! Generated number is below 3.")
                    return
                else:
                    retry_count += 1
                    print(f"Retry {retry_count}: Generated number is {result}.")
            print(f"Max retries reached. Exiting function.")
        return wrapper
    return decorator_retry

@retry(max_retry=3)
def generate_random_number():
    return random.randint(1, 10)

# Call the decorated function
def main():
    generate_random_number()
if __name__ == "__main__":
    main()