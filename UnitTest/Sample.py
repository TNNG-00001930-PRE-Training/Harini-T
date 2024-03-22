def slicing(s):
    string=s[2:]
    return string
def formatting(s):
    k=('Hello welcome to {}'.format(s))
    return k
def concatenation(s):
    return "Happy Coding "+s
def manipulation(s):
    u=s.upper()
    l=s.lower()
    st=s.strip()
    r=s.replace('a','h')
    lis=[u,l,st,r]
    return ",".join(lis)
s=input("Enter a string:")
print(slicing(s))
print(formatting(s))
print(concatenation(s))
print(manipulation(s))