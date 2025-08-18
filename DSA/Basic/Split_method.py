'''
The split method breaks up a string at specified separator and return a list of string.
--> string.split(separator,maxsplit)
--> Separator: optional hota hai, by default whitespace hota hai (break kha se karna hai )
--->Maxsplit: optional hota hai, by default whitespace hota hai(kitne split karane hai)
'''
msg="i want to become python programmer"
l=msg.split()
print(l)
print(len(l))

msg1="india,pakistan,usa,shrilanka"
l1=msg1.split(',')
print(l1)
print(len(l1))

msg2="india,pakistan,usa,shrilanka"
l2=msg1.split(',',2)
print(l2)
print(len(l2))