n = int(input())

if (n < 0) and (n%2==0):
    print('A')
elif (n < 0) and (n%2!=0):
    print('B')
elif (n > 0) and (n%2==0):
    print('C')
elif (n > 0) and (n%2!=0):
    print('D')