class A:
    def func(self,nums):
        if nums==0 or nums==1:
            return nums
        return self.func(nums-1)+self.func(nums-2)

    def fib(self,n):
        ans=self.func(n)
        return ans
obj=A()
print(obj.fib(6))
## TC= o(2^n) --> fun(10)=fun(9)+fun(8)-->2 fun add or vo repeat ho rhe hai
##SC=o(2^n)

##normal function
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(int(input("Enter a number:"))))