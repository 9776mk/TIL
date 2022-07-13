c = int(input(), 16)


#hex_list = {'A':10, 'B':11,'C':12, 'D':13, 'E':14, 'F':15}
#n = input()
#c = hex_list[n]

for i in range(1,16):
    print('%X'%c, '*%X'%i, '=%X'%(c*i), sep='')