n = int(input())
l = []
vow = ['a', 'e', 'i', 'o', 'u']
for i in range(n):
    l.append(input())
pre = []
for j in range(n):
    for i in range(len(l[j])):
        if l[j][i] in vow :
            pre.append(l[j])
pre = list(set(pre))
if len(pre) == len(l):
    print("No values")
else:
    for i in range(n):
        if l[i] in pre:
            pass
        else:
            print(l[i])