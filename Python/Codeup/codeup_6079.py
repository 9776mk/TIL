n = int(input())
sum = 0
count = 1

q_bool = False

while q_bool!= True:
    sum += count
    if (sum >= n):
        print(count)
        q_bool=True
        break
    else:
        count += 1