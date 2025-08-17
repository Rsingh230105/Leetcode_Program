'''
#head 1 to n
def fun(i,n):
    if i<=n:
        print(i)
        i+=1
        fun(i,n)

fun(1,15)
print("\n")

##orrr  1 to n head recursion
def fun(i, n):
    if i > n:
        return
    print(i)
    fun(i+1, n)


fun(1, 15)
'''
'''
## using tail recursion return n to one like 15 to 1
def fun(i, n):
    if i > n:
        return
    fun(i+1, n)
    print(i)

fun(1, 15)
'''
##head n to 1
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(5)

## one to n using tail
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)

fun(5) 

