l=["A","B","C"]
s=":".join(l)
print(s)

'''
-->join method ka use karke hum kisi bhi iterator ko string me convert karte hai
--->Join method hame string return karta hai
-->seperator.join(iterator)
---> iterator ke item string hi hone chahiye othewise erro dega
'''
l1=["P","Y","T","H","O","N"]
s1="".join(l1)
print(s1)

s={"bharat","Mata","Ki","Jay"}
s1="-->".join(s)
print(s1)

d={"india":2000,"america":150,"Nepal":500}
s2=" ".join(d)##ye hame key return karega
print(s2)