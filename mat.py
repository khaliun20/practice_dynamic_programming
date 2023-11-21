import sys
import time
from functools import cache



def format_matrices(file_content):
    lines = file_content.strip().split('\n')
    if not lines:
        raise ValueError("File is empty")
    matrices = []
    for i, line in enumerate(lines):
        name, x, y = line.split(",")
        matrices.append((name, int(x), int(y)))
    return matrices

@cache
def matrix_chain(matrices):

    if i == j:
        return 0
    min_val = float('inf')
    for k in range(i, j):
        count = (MatrixChain(p, i, k) +
                 MatrixChain(p, k+1, j) +
                 p[i-1]*p[k]*p[j])
        if count < min_val:
            min_val = count
    return min_val

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mat.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()        
        matrices = format_matrices(file_content)
        tuple_matrices = tuple(matrices)
        start_time = time.perf_counter_ns()
        matrix_chain(tuple_matrices)      
        end_time = time.perf_counter_ns()

        print(end_time - start_time)
    except FileNotFoundError:
        print(f"Error: File not found: {test_file}")
        sys.exit(1)
    except ValueError as e:
        print(f"ValueError: {str(e)}")
        sys.exit(1)
