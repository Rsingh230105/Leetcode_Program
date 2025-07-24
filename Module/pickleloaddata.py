import pickle

file=open("writedata.txt","rb")# read data binary from writedata.txt file

l=pickle.load(file)
print(l)
