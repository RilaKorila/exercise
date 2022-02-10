class Fibonacci:
    # recursive solution
    # O(n^2): the larger n is, the more time it takes to solve the problem
    def recursion_fib(self, n:int)->int:
        # base case
        if n<=1:
            return 1
        else:
            return self.recursion_fib(n-1) + self.recursion_fib(n-2)
    
    # variables memo is necessary to memorization solution
    memo = [0 for i in range(50)]
    
    # memorization
    def memo_fib(self, n:int)->int:
        
        
        if n<=1:
            return 1
        else:
            # if fib(n) is not memorized, write it down
            if self.memo[n] == 0:
                self.memo[n] = self.memo_fib(n-1) + self.memo(n-2)
            return self.memo[n]
    
    
    # Dinamic Programming
    def dp_fib(n: int)->int:
        a = [1]*(n+1)
        
        for i in range(2, n+1):
            a[i] = a[i-1] + a[i-2]
        
        return a[n]