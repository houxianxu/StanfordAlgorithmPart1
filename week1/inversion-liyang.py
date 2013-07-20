import time
def sort_and_count(a):
    n=len(a)
    if n==1:
        return [0,a]
    else:
        x=sort_and_count(a[0:n/2])
        y=sort_and_count(a[n/2:])
        z=merge(x[1],y[1])
        return [x[0]+y[0]+z[0],z[1]]
def merge(a,b):
    i=0
    j=0
    c=[]
    d=0
    while 1:
        if a[i]<=b[j]:
            c+=[a[i]]
            i+=1
        else:
            c+=[b[j]]
            d+=len(a)-i
            j+=1
        if i==len(a):
            c=c+b[j:]
            break
        if j==len(b):
            c=c+a[i:]
            break
    return [d,c]

file_name = 'IntegerArray.txt'
inputfile=open(file_name,'r')
b=[]
for line in inputfile:
    data=int(line.strip())
    b.append(data)
inputfile.close()
start_time=time.time()
print sort_and_count(b)[0]
end_time=time.time()
print end_time-start_time

