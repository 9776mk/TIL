w, h, b = map(int, input().split())

total_store = w * h * b
mb_store = total_store/8/1024/1024

print(f'{mb_store:.2f} MB')