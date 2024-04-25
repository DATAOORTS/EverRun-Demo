import time
import helping

start_time = time.time()

helping.python_version()  # This will print Current Python Version
helping.fibonacci_box()   # This will print Fibonacci sequence of numbers inside numbers.txt file at output.txt file

end_time = time.time()
execution_time = end_time - start_time

print("Task Completed Successfully")
print("Total execution time:", execution_time, "seconds")
