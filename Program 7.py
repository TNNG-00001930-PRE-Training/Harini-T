def even_numbers():
    l=[]
    for i in range(1000,3001):
        if i%2==0:
            l.append(i)
    return l
v=even_numbers()
print(','.join(map(str, v)))