import random as r
SystemInput=r.randrange(1,101)

UserInput=int(input("Enter the Number:"))
print(SystemInput)
if SystemInput==UserInput:
    print("both are equal")
elif SystemInput>UserInput:
    print("System input is High")
else:
    print("User inpute is High")


