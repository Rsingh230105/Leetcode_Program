##using while loop
# name=input("enter your name:")
# print("original String:",name)
#
# r_name=""
# c=len(name)
#
# while c>0:
#     r_name=r_name+name[c-1]
#     c-=1
# print(r_name)

##for loop

name=input("enter your name:")
print("original String:",name)
rev=""

for i in name:
    rev=i+rev

print(rev)

##slising method
name=input("enter your name:")
print("original String:",name)

print(name[::-1])