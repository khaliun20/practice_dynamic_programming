import time, sys
from functools import cache

class TreeNode:
    def __init__(self, val, freq, left, right):
        self.val=val
        self.freq=freq
        self.left=left
        self.right=right
        self.cost = None
        pass
    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        left = str(self.left) if self.left is not None else '()'
        right = str(self.right) if self.right is not None else '()'
        return '({} {} {})'.format(self.val,left,right)
        
    def computeCost(self):
        if self.cost is not None:
            return self.cost
        def helper(n,depth):
            if n is None:
                return 0
            return depth * n.freq + helper(n.left, depth+1) + helper(n.right, depth +1)
        self.cost = helper(self, 1)
        return self.cost
    pass
pass

@cache
def build_optimal_tree(nodes, freq, i, j):
    # Base case
    if j < i:
        return None, 0

    min_cost = float('inf')

    # Recursive case
    for k in range(i, j + 1):
        left_subtree, left_cost = build_optimal_tree(nodes, freq, i, k - 1)
        right_subtree, right_cost = build_optimal_tree(nodes, freq, k + 1, j)
        cost = left_cost + right_cost + sum(freq[i:j + 1])

        if cost < min_cost:
            min_cost = cost
            optimal_root = TreeNode(nodes[k], freq[k], left_subtree, right_subtree)

    return optimal_root, min_cost

def main():
    if len(sys.argv) != 2:
        print("Usage: python tree.py <filename>")
        return

    filename = sys.argv[1]
    tree = {}
    with open(filename, 'r') as file:
        for line in file:
            node, frequency = line.strip().split(':')
            tree[int(node)] = int(frequency)
    i = 0 
    j = len(tree) -1
    start_time = time.perf_counter_ns()
    root, cost = build_optimal_tree(tuple(tree.keys()), tuple(tree.values()),i,j)
    end_time = time.perf_counter_ns()
    print(str(root))
    print(root.computeCost())
    print(end_time - start_time)
    

if __name__ == "__main__":
    main()

