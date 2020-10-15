def missing_digits(n):
    if n<10:
        return 0
    rest,last=n//10,n%10
    return max(last-rest%10-1,0)+missing_digits(rest)