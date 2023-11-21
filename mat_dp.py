import sys
import time

def matrix_multiplication(matrices):
    n = len(matrices)
    dp = [[float('inf')] * n for _ in range(n)]
    brackets = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrices[i][1] * matrices[k][2] * matrices[j][2]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    brackets[i][j] = k

    def construct_expression(i, j):
        if i == j:
            return matrices[i][0]
        else:
            return "(" + construct_expression(i, brackets[i][j]) + "*" + construct_expression(brackets[i][j]+1, j) + ")"

    return construct_expression(0, n-1), dp[0][n-1]

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

    start_time = time.perf_counter_ns()
    expression, operations = matrix_multiplication(matrices)
    end_time = time.perf_counter_ns()

    print(expression, operations)
    print(end_time - start_time)

if __name__ == "__main__":
    main()
