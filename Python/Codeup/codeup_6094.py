n = int(input())
a = list(map(int, input().split()))

#print(min(a))


min_num = a[0]

for i in range(n-1):
    if a[i] > a[i+1]:
        min_num = a[i]
    else:
        continue

print(min_num)