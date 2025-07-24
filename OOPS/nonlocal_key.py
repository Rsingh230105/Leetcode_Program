def myfun1():
    x="jay hind"
    def myfun2():
        nonlocal x
        x="jay bharat"
    myfun2()
    return x

print(myfun1())
# outer function ka use karke inner function ke variable ko print kra sakte hai with the help of nonlocal keyword