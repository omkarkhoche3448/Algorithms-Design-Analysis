
def knapsack(wt, val, W, n):

    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)     
        return t[n][W]

# Driver code
if __name__ == '__main__':
    profit = [1,4,5,7,4]
    weight = [1,3,4,5,2]
    W = 50
    n = len(profit)
    
    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    print(knapsack(weight, profit, W, n))

# Output : 21


# What is the base case for the recursive knapsack algorithm?
# The base case occurs when there are no items (n == 0) or the knapsack's weight capacity is zero (W == 0), where the result is 0.

# What is memoization, and why is it used here?
# Memoization is the process of storing the results of subproblems in a table (t) to avoid redundant calculations. It helps optimize the algorithm by ensuring each subproblem is solved only once.

# How does the algorithm decide whether to include or exclude an item?
# If the item's weight is less than or equal to the knapsack’s remaining capacity, the algorithm makes two recursive calls: one for including the item and one for excluding it, and chooses the maximum value from these two choices.

# What is the time complexity of this solution?
# The time complexity is O(n * W), where n is the number of items and W is the capacity of the knapsack.

# Can you explain the role of the t[n][W] table?
# The table t[n][W] stores the maximum value that can be achieved with the first n items and a knapsack of capacity W. It is used for memoization to avoid recalculating the same subproblems.

# What happens if the weight of an item is greater than the remaining capacity of the knapsack?
# If an item's weight exceeds the remaining capacity of the knapsack, it cannot be included in the solution. The algorithm will recursively solve the problem without that item
