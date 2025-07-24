def pd(st):
    return st==st[::-1]
def palin(s):
    a=s
    fs=''
   
   
    
    for i in range(len(a)):
        for j in range(i,len(a)+1):
            cs=a[i:j]
            if pd(cs) and len(cs)>len(fs):
                fs=cs
    return fs

s='babadadab'
print(palin(s))