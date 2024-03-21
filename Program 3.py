def list_tuple():
    n=input("Enter numbers seperated by comma:")
    l=[int(i) for i in n.split(',')]
    t=tuple(l)
    print(l)
    print(t)
list_tuple()