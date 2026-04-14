""" 
    Application entry point for the day2 project.
"""

def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


if __name__ == "__main__":
    n = 10
    print(f"The {n}th Fibonacci number is: {fib(n)}")