- for : 순회 할때(문자열/리스트 등) + 횟수를 알 때(range)
- while : 조건에 도달할 때까지 (while True + break)


# API
- Application Programming Interface 응용 프로그램 인터페이스
  - 컴퓨터나 컴퓨터 프로그램 사이의 연결
  - 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공
  - 사용하는 방법을 기술하는 문서나 표준은 API 사양/명세(specification)

- API를 사용하기 전에 확인해야 할 것? 어떻게 조작하는지!
- 주소로 요청을 보내면 문서로 응답해준다!
- 그림 추가

## API 활용시 확인 사항
- 요청하는 방식에 대한 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하는 기능에 대한 추가 경로
    - 요청 변수(필수와 선택)

- 응답 결과에 대한 이해
  - 응답 결과 타입 (JSON)
  - 응답 결과 구조


```python
# pip install requests # 안했으면 설치하기
import requests
# URL로
order_currency = 'BTC'
payment_currency = KRW
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{paymen_currency}'
# 요청을 보내서
response = requests.get(URL) # http 메서드가 get이면 .get, post면 .post(URL) 사용
#응답 받은 값을 가져온다.
print(response, type(response)) # <Response[200]> <class 'requests.models.Response'>

# 속성 예시
print(response.status_code) # 200
print(response.txt, type(response.txt)) # 문자열

# 메서드 예시
# .json() 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경!
print(response.json(), type(response.json())) # <class 'dict>

print('===================================================')

data = response.json()
# data는 딕셔너리 => 키로 접근
print(data.keys()) #[status, data]
print(data.get('data'))
print(data.get('data').get('closing_price'))
```

```python
import requests
order_currency = 'ALL'
payment_currency = KRW
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{paymen_currency}'
response = requests.get(URL).json()
print(response)
print(response.get('data'))

coins = response.get('data')

# coins : 딕셔너리
# key : coin이름
# value :  딕셔너리(코인의 정보)
for coin in coins:
  # coins.get(coin) <- 코인의 정보인 딕셔너리
  # 그 딕셔너리의 closing price

  if coin == 'date':
    conintue
  print(coin, coins.get(coin).get('closing_price')) # AttributeError : 'str' object has no attribut 'get' coins 혹은 coins.get(coin)이 문자열
  # print(coin) # date : '숫자숫자'가 있음
```


```python
#https://api.agify.io?name=michael

import requests
URL = 'https://api.agify.io'
params = {
  'name' : 'michael'
}
response = requests.get(URL, params=params)
print(response)
```
```python
print('나이를 알려드립니다.')
name = input('이름을 알려주세요')
print('=====================')
# random.seed(0) 랜덤 값을 고정
print(f'{random.choice(range(10,90))}살 입니다.') #choice(a)는 하나 고르기, sample(a,b)는 a에서 b개 고르기
```


# TMDB 사용 실습
```python
# 키값 : 복사해서 사용!
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# movies에 많이 있음
import requests

BASE_URL = 'https://api.themoviedb.org/3/'
path = '/movie/76341'
# path = 'movie/popular'
params = {
  'api_key : '~~~~~~~'
  'language' : 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)
```


```python
import requests

# 랜덤 한 번호 고르고

# 실제로 내가 1024회동안 해당 번호로 샀으면 얼마를 벌었을까?
# 1~5등

for n in range(1,10):
  URL = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo]{n}'
  response = requests.get(URL).json()
  print(response)
```