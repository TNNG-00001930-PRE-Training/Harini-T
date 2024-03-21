import re
def password_regex(txt):
    if len(txt)>=6 and len(txt)<=12:
        p= re.findall("[a-z]", txt)
        q= re.findall("[A-Z]",txt)
        r=re.findall("[0-9]",txt)
        s=re.findall("[#$@]",txt)
        if p:
            if q:
                if r:
                    if s:
                        return True

        return False



def password_checker():
    txt = input("Enter passwords by seperating comma:")
    l=list(txt.split(','))
    k=[]
    for i in l:
        if password_regex(i):
            k.append(i)
    return ",".join(k)
print(password_checker())
    
