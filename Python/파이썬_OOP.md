# OOP

- 객체 지향 프로그래밍

- Object Oriented Programming

- 파이썬은 모든 것이 객체(object)

- 객체(컴퓨터 과학) : 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것
  
  - 특정 타입(클래스)의 인스턴스이다.

- 객체 지향 프로그래밍 : 컴퓨터 프로그램을 여러 개의 독립된 단위, 즉 객체들의 모임으로 파악하고자 하는 것.

- 타입(종류)과 값(실제 사례) = class와 instance

## 객체

- 객체의 특징
  
  - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능하가?
  
  - 속성(attribute) : 어떤 상태를 가지는가?
  
  - 조작법(method) : 어떤 행위를 할 수 있는가

### 객체 지향 프로그래밍

- 객체 지향 프로그래밍이란?
  
  - 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

- 절차지향 프로그래밍 : 데이터와 함수로 인한 변화

- 객체지향 프로그래밍 : 데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스)

- 현실 세계를 프로그램 설계에 반영(추상화)

```python
  class Person:
      def __init__(self, name, gender):
          self.name = name
          slef.gender = gender

      def greeting_message(self):
          return f'안녕하세요, {self.name}입니다.'

  jimin = Person('지민, '남')
   print(jimin.greeting_message()
```

```python
# 사각형 넓이 길이 구하기

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
```

- 사각형 - **클래스(class)**

- 각 사각형(R1, R2) - **인스턴스(instance)**

- 사각형의 정보 - **속성(attribute)**
  
  - 가로 길이, 세로 길이

- 사각형의 행동/기능 - **메소드(method)**
  
  - 넓이를 구한다. 높이를 구한다.

  인스턴스의 속성들을 메소드를 통해 활용한다.

## OOP 기초

### 기본 문법

```python
# 클래스 정의
class Myclass:
    pass
# 인스턴스 생성
my_instance = MyClass()
#메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute
```

- CamelCase : 클래스(대문자)

- snake_case : 변수/함수

### 클래스와 인스턴스

- 클래스 : 객체들의 분류(class)

- 인스턴스 : 하나하나의 실체/예(instance)

- **파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스**

```python
class Person:
    pass
print(type(Person)
#type
p1 = Person()
type(p1)
# __main__.Person
isinstance(person1, Person)
# True
```

### 속성

- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

```python
class Person:

    def __init__(self, name):
        self.name = nmae


person1 = Person('지민')
person1.name #'지민'
```

### 메소드

- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

- 클래스 내부에 정의된 함수

```python
class Person:


    def talk(self):
        print('안녕')
    def eat(self, food):
        print(f'{food}를 냠냠')


person1 = Person()
person1.talk() # 안녕
person1.eat('피자') # 피자를 냠냠
person1.eat('치킨') # 치킨를 냠냠
```

### 객체 비교하기

- ==
  
  - 동등한(equl)
  
  - 변수가 참조하는 객체가 동등한 (내용이 같은) 경우 True
  
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님

- is
  
  - 동일한(identical)
  
  - 두 변수가 동일한 객체를 가리키는 경우 True

```python
b[a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b) # True False

# 얕은 복사
a = [1, 2, 3]
b = a
print(a==b, a is b) #  True True
b[0] = 'hi'

# list 형변환 결과 : 사실은 list고, 사실은 값도 같지만 
# 다른 메모리 주소 결과를 받아냄
c = [3,4,5]
d = list(c)
d[0] = 'hi'


# 슬라이싱
e = [4,5,6]
f = e[::]
f[0] = 'hi'


# 깊은 복사
a = [[1,2], 2, 3]
b = list(a)
b[0][0] = 'hi'


import copy
c = [[1,2], 2, 3]
d = copy.deepcopy(c)
d[0][0] = 'hi'
```

- 깊은 복사

- 얕은 복사

변수 - 메모리 주소값



### 인스턴스

#### 인스턴스 변수

- 인스턴스가 개인적으로 가지고 있는 속성(attribute)

- 각 인스턴스들의 고유한 변수

- 생성자 메소드에서 self.<name>으로 정의

- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당



```python
class Person:
    def __init__(self, name):
        self.name = name # 인스턴스 변수 정의
john = Person('john')
print(john.name) # john #인스턴스 변수 접근 및 할당
john.name = 'John Kim' # 인스턴스 변수 접근 및 할당
print(john,name) # John Kim
```

#### 인스턴스 메소드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드

- 클래스 내부에 정의되는 메소드의 기본

- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

```python
class MyClass
    def instance_method(self, arg1, ...)


my_instance = MyClass()
my_instance.instance_method(...)
```

#### self

- 인스턴스 자기자신

- 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
  
  - 매개변수 이름으로 self를 첫번째 인자로 정의
  
  - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

#### 생성자(constructor) 메소드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드

- 인스턴스 변수들의 초기값을 설정
  
  - 인스턴스 생성
  
  - __init __ 메소드 자동 호출

```python
class Person:
    def __init__(self):
        print('인스턴스가 생성되었습니다.')
person1 = Person() #인스턴스가 생성되었습니다.

class Person:
    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')
person1 = Person('지민') #인스턴스가 생성되었습니다. 지
```

#### 소멸자(destructor) 메소드

- 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

```python
class Person:
    def __del__(self):
        print('인스턴스가 사라졌습니다.')


person1 = Person()
del person1 #인스턴스가 사라졌습니다.
```
