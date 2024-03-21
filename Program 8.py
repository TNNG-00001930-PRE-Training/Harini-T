import re
txt = input()
x = re.findall("[a-z]", txt)
y= re.findall("[A-Z]",txt)

print("LOWER CASE:",len(x))
print("UPPER CASE:",len(y))
