f=open('data.txt',mode='r')
number_of_words=0
number_of_chars=0
number_of_lines=0

for line in f:
    number_of_lines=number_of_lines+1
    line=line.strip()##ye \n or space ko by default ignore kar deta hai
    if line in "hello world":
        print("hello is present in the file line 1")

    length=len(line)

    number_of_chars=number_of_chars+length

    list1=line.split()
    number_of_words=number_of_words+len(list1)


f.close()
print("number_of_lines:-",number_of_lines)
print("number_of_words:-",number_of_words)
print("number_of_chars:-",number_of_chars)##space bhi count karega
