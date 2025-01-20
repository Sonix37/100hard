f=open('09(1).txt')
k=0
for s in f:
    st=sorted(int(x) for x in s.split())
    if st[0]>3:
        k+=1
print(k)
