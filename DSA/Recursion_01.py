#Head recursion
c=0
def fun():
    global c
    if c == 4:
        return
    print("Ram")
    c+=1
    fun()

fun()

### if c ko function ke under initialize karte to 987 ke around times chalta
### Tail recursion
# c = 0
# def fun():
#     global c
#     if c == 4:
#         return
#     c += 1
#     fun()
#     print("Ram")
#
# fun()