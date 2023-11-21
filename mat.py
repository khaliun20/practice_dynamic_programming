import sys
import time
from functools import cache

@cache
def matrix_multiplication(matrices, i, j):
    if i == j:
        return matrices[i][0], 0 
    else:
        min_cost = float('inf')
        min_expression = ""
        for k in range(i, j):
            left_expr, left_cost = matrix_multiplication(matrices, i, k)
            right_expr, right_cost = matrix_multiplication(matrices, k+1, j)
            current_cost = matrices[i][1] * matrices[k][2] * matrices[j][2]
            total_cost = left_cost + right_cost + current_cost

            if total_cost < min_cost:
                min_cost = total_cost
                min_expression = f"({left_expr} * {right_expr})"
        
        return min_expression, min_cost

def main():
    if len(sys.argv) != 2:
        print("Usage: python mat2.py <filename>")
        return

    filename = sys.argv[1]
    matrices = []

    with open(filename, 'r') as file:
        for line in file:
            name, rows, columns = line.strip().split(',')
            matrices.append((name, int(rows), int(columns)))

    matrices = tuple(matrices) 

    start_time = time.perf_counter_ns()
    expression, operations = matrix_multiplication(matrices, 0, len(matrices)-1)
    end_time = time.perf_counter_ns()

    print(expression)
    print(operations)
    print(end_time - start_time)

if __name__ == "__main__":
    main()
