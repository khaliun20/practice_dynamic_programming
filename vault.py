import sys
import time
from functools import cache


def get_vault_dim(file_content):
    lines = file_content.strip().split('\n')
    if not lines:
        raise ValueError ("File is empty")
    first_line = lines[0].strip()
    num_col = len(first_line.split(','))
    num_row = len(lines)
    return num_col, num_row

def convert_to_matrix(num_col, num_row, file_content):
    global vault_matrix
    vault_matrix = []

    lines = file_content.strip().split('\n')
    for line in lines:
        values = list(map(int, line.strip().split(',')))
        vault_matrix.append(values)

@cache
def find_optimal_path(col, row):
    #base case
    if col < 0 or row < 0:
        return 0, ""

    #recursive case 
    move_north, path_north = find_optimal_path(col, row - 1)
    move_west, path_west = find_optimal_path(col - 1, row)

    if move_north >= move_west:
        return vault_matrix[row][col] + move_north, path_north + "N"
    else:
        return vault_matrix[row][col] + move_west, path_west + "W"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vault.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        num_col, num_row = get_vault_dim(file_content)
        convert_to_matrix(num_col, num_row, file_content)

        start_time = time.perf_counter_ns()
        max_gold, optimal_path = find_optimal_path(num_col - 1, num_row - 1)
        end_time = time.perf_counter_ns()

        print(optimal_path[1:][::-1])
        print(max_gold)
        print(end_time - start_time)
    except FileNotFoundError:
        print(f"Error: File not found: {test_file}")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)