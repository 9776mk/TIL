## Namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는
  경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음

- app_name attribute를 작성해 URL namespace를 설정

![](django_05.assets/1.PNG)

### URL tag 변화

![](django_05.assets/2.PNG)

![](django_05.assets/3.PNG)

### URL 참조

- ":" 연사자를 사용하여 지정
  
  - 예를 들어, app_name이 articles이고 URL name이 index인 주소 참조는 articles:index가 됨

## Naming URL patterns

### Naming URL patterns의 필요성

- 예를 들어 "index/"의 문자열 주소를 "new-index/"로 바꿔야 한다고 가정하면
  
  - "index/" 주소를 사용한 모든 곳을 찾아서 변경해야 함!

### Naming URL patterns

- 링크에 URL을 직접 작성하는 것이 아니라 “path()” 함수의 name 인자를 정의해서 사용

- DTL의 Tag 중 하나인 URL 태그를 사용해서 “path()” 함수에 작성한 name을 사용할 수 있음

- 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음

- Django는 URL에 이름을 지정하는 방법을 제공함으로써 view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

![](django_05.assets/4.PNG)

### Built-in tag - "url"

![](django_05.assets/5.PNG)

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환

- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 `링크를 출력하는 방법
  ![](django_05.assets/6.PNG)

- [참고] DRY 원칙
  
  - Don't Repeat Yourself 약어
  
  - 소스 코드에서 동일한 코드를 반복하지 말자는 의미

## Model

- Django는 model을 통해 데이터에 접근하고 조작

- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함

- 저장된 데이터베이스의 구조 (layout)

- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
  
  - 모델 클래스 1개 == 데이터베이스 테이블 1개
  - 매핑 : 하나의 값을 다른 값으로 대응시키는 것
    ![](django_05.assets/6.PNG)
