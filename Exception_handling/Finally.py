def fun1():
    try:
        l=[1,2,3,4]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
   # without finally keyword (I am always executed nahi chalega ) function ke bhar chala sakte ho
    finally:
        print("I am always executed")

x=fun1()
print(x)

