import sys

def python_version():
    print("Python version:", sys.version)
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_box(input_file="numbers.txt", output_file="output.txt"):   # For Getting all values in output.txt{Auto-Generate} file
    with open(input_file, "r") as infile:
        numbers = [int(line.strip()) for line in infile]

    with open(output_file, "w") as outfile:
        for num in numbers:
            result = fibonacci(num)
            outfile.write(f"Fibonacci({num}) = {result}\n")
