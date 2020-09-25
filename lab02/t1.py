def cycle(f1, f2, f3):
    def fun_c(n):
        def fun_t(x):
            if n==0:
                return x
            for i in range(1,n+1):
                if i%3==1:
                    x=  f1(x)
                elif i%3==2:
                    x= f2(x)
                else:
                    x= f3(x) 
            return x
        return fun_t
    return fun_c

def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3
my_cycle = cycle(add1, times2, add3)
identity = my_cycle(2)

print(identity(1))
