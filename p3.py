n=int(input())
T = {}
root=set(range(1,n+1))
#a=[]
for i in range(1,n+1):
    line = input().split()
    n_line = list(map(int,line)) [1:]
    T[i] = n_line
#    a=a+n_line
    root=root-set(n_line)
      
#for i in range(1,n+1):
#    if i in a:
#        pass
#    else:
#        print(i)


def h(v):
    if (T[v]==[]):
        return 0
    else:
        return max(map(h,T[v]))+1

print(root.pop())
print(sum(map(h, range(1,n+1))))
