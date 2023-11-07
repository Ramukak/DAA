def fibonacci_non_recursive(n):
    if n <= 1:
        return n
    fib_0 = 0
    fib_1 = 1
    for i in range(2, n+1):
        fib_i = fib_0 + fib_1
        fib_0, fib_1 = fib_1, fib_i
    return fib_1

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_non_recursive(50))
print(fibonacci_recursive(50))

'''
Non-Recursive Implementation:
Time Complexity: O(n) - The loop runs from 2 to n, performing constant-time operations in each iteration.
Space Complexity: O(1) - Only a constant amount of extra space is used to store variables (fib_0, fib_1, fib_i).
Recursive Implementation:
Time Complexity: O(2^n) - This is because the recursive function calls itself twice for each value of n.
Space Complexity: O(n) - The maximum depth of the recursive call stack is n, as it goes all the way down to 0.
Conclusion:
The non-recursive implementation is more efficient in terms of both time and space complexity compared to the recursive implementation. The recursive implementation has exponential time complexity, which makes it impractical for large values of n due to its high computational cost.
The non-recursive implementation, on the other hand, has linear time complexity, which means it can handle much larger values of n efficiently. Additionally, it has constant space complexity, making it more memory-efficient.
If you were to calculate Fibonacci numbers for large values of n, it is recommended to use the non-recursive implementation.
'''