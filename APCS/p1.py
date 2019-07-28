# coding: utf-8
m = input()
n = m.split()

o=[]
for i in n:
    k=f'{int(i):0>5}'
    o.append(k)

o.sort()

p=[]
for j in o:
    k=int(j)
    p.append(k)

print(p[0],p[1],p[2])

if int(p[0]) + int(p[1]) < int(p[2]):
    print("No")
elif int(p[0])**2 + int(p[1])**2 < int(p[2])**2:
    print("Obtuse")
elif int(p[0])**2 + int(p[1])**2 > int(p[2])**2:
    print("Acute")
else:
    print("Right") 
