자습서

MIT python

파이썬 자습서(공식문서)

점프 투 파이썬(온라인 책)

파이썬 코딩도장(온라인 책)

한 줄 주석 처리

Ctrl + /

# 16진수 입력

```python
n = int(input, 16)
```

# 소수 n번째까지 출력

- fstring

```python
{변수:.nf}
```

# 파이썬 리스트 초기화

```python
a = list()
#0으로 초기화
for i in range(10):
    a.append(0)
```

## 2차원

```python
# n x m 2차원 리스트 초기화
n = 3
m = 4
arry = [[0] * m for _ in range(n)]
```

# 글자 거꾸로 쓰기

```python
word = 'dsfdjkljafkl'
for char in (len(word)):
print(word[len(word)-i-1])
```

# 반복문으로 여러 줄 입력받을 때

- input() 함수로는 시간초과가 발생할 수 있음(ex [백준 15552번 문제](https://www.acmicpc.net/problem/15552))
- sys.stdin.readlin()을 사용
- [참고 사이트](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)

```python
import sys
a = int(sys.stdin.readline()) #한 개의 정수 #3\n이 입력 및 str형태로 저장되기 때문에 int로 형변환
n,m,l = map(int,sys.stdin.readline().split()) #여러 개의 정수
k = list(map(int,sys.stdin.readline().split())) #임의의 개수의 정수

#임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

#문자열 n줄을 입력받아 리스트에 저장할 때
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
```

# try ~ except ~

```python
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
```

- 백준 10951
- 오류 처리를 위한 구문
- try 블록 수행 중 오류가 발생하면 excpet 블록이 수행됨.

# 딕셔너리 활용

```python
word = 'banana'
result = {}
for char in word:
# result[char] # 없으면 keyError
# result.get(char, 0) #없으면 None, 기본값을 주면 0

result[char] = result.get(char, 0) + 1
# result 딕셔너리에서 char 키에 해당하는 value를 가져오기.
# 만약 value값이 없으면 0으로 초기화, 
# 있으면 result[char]에 +1을 한 뒤 추가 
```

```python
for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1
```

# 리스트 안의 key를 이용해 value 값 꺼내기

```python
list[index]['키']
```

# 파일 읽기

```python
import sys
sys.stdin = open("파일명.txt, "r")
```
