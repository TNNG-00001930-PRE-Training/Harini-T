def even_length(s):
    s=s.split()
    for i in s:
        if len(i)%2==0:
            print(i)
s="Python is a programming language"
even_length(s)