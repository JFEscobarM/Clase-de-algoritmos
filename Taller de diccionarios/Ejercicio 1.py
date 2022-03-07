list=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23] 
cantidad={}


for n in list:
    if n in cantidad:
        cantidad [n]+=1
    else:
        cantidad [n]=1
print(cantidad)