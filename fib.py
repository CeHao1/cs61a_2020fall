def fib(n): # recursive fib without storage
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
def fib_s(n):  # Iterative fib with storage
    d={0:0,1:1}
    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]

def fib_r(n): # recursive fib with storage
    d0={-2:-1,-1:1}
    def helper(i,d):
        if i>n: # stop recursion
            return d[n]
        else:
            d[i]=d[i-1]+d[i-2]
        return helper(i+1,d)
    return helper(0,d0)
