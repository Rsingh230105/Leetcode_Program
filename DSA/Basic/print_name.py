c=0
def fun(n):
    global c
    if n<=10 and n>0:
        print("Rajendra",c)
        c=c+1
        fun(n-1)
fun(10)

