#remove duplicates:
s='hello world hello world good morning good afternoon'
s=s.split()
s1=''
for i in s:
    if i not in s1:
        s1=s1+i+' '
print(s1)
