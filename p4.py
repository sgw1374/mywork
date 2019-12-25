from itertools import permutations

N=int(input())
w_str=input().split()
f_str=input().split()

w=list(map(int, w_str))
f=list(map(int, f_str))

stacks= list(permutations(range(N)))

def energy(s):
    e=0
    for k in range(1,N):
        weight=0
        for i in range(k):
            weight=weight + w[s[i]]        
        e=e+f[s[k]]*weight  
               
    return e

minn=min(map(energy,stacks))
print(minn)
