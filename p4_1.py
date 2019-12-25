from itertools import permutations

N=int(input())
w_str=input().split()
f_str=input().split()

w = lambda k:int(w_str[k])
f = lambda k:int(f_str[k])

stacks = list(permutations(range(N)))

def energy(s):
    e = 0
    for k in range(1,N):
        weight = sum(map(w,s[0:k]))
        e = e + weight*f(s[k])
    return e

minn=min(map(energy,stacks))
print(minn)
