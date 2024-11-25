def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)
    z2 = karatsuba(high1, high2)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2)) - z0 - z2
    multiplication = (z2 * 10 ** (2 * half) + z1 * 10 ** half + z0)
    return multiplication
if __name__ == "__main__":
    num = input("Enter Multiplication :- ")
    x, y = num.split("x")
    mul = karatsuba(int(x.strip()), int(y.strip()))
    print(f"{num} = {mul}")


# divide-and-conquer strategy (Splitting the numbers),base case handles small numbers (less than 10) no use of recursion. 
# algorithm first calculates the maximum length of the two numbers and splits them into halves
# "high" part (the left side) and the "low" part (the right side). This is done using the divmod function, which divides the number by 10 half 
# and returns the quotient and remainder (high and low parts).
# The algorithm recursively multiplies the high and low parts of both numbers:
# z2: This is the product of the high parts of x and y.
# z0: This is the product of the low parts of x and y.
# z1: This is the product of the sum of high and low parts of x and y. 
# The final multiplication step subtracts the previously computed z2 and z0 to avoid double-counting.
# Combines the three partial results (z2, z1, and z0)

# ≈O(n^1.585),
# 𝑂(𝑛2)
 # 𝑂(𝑛2)