def fun(sum,i,n):
    if i>n:
        print(sum)
        return
    sum += i
    fun(sum,i+1,n)


fun(0,1,10)

## method 2
def fun(n):# TC=o(n), SC=o(n) because stack overflow
    if n==1:
        return 1
    return n+fun(n-1)

print(fun(10))