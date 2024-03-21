def sorted_strings(s):
    s=list(s.split(','))
    s=sorted(s)
    return ",".join(s)
s=input("Enter the words by using comma as a seperator:")
print(sorted_strings(s))