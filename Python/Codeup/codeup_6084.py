h, b, c, s = map(int, input().split())

file_store = h * b * c * s

mb_store = file_store/8/1024/1024

print(f'{mb_store:.1f} MB')
