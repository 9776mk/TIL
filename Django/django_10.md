## 로그인에 대한 이해

### HTTP

- Hyper Text Transfer Protocol

- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)

- 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초

- 클라이언트 - 서버 프로토콜이라고도 부름

### 요청과 응답

- 요청 (requests)
  
  - 클라이언트(브라우저)에 의해 전송되는 메시지

- 응답 (response)
  
  - 서버에서 응답으로 전송되는 메시지

### HTTP 특징

- 비연결지향(connectionless) 
  
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  
  - 예를 들어 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아님
  
  - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것

- 무상태(stateless) 
  
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
  
  - 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

- 서버와 클라이언트 간 지속적인 상태 유지를 위해 쿠키와 세션이 존재

### 쿠키

- 서버가 사용자의 웹 브라우저(클라이언트)에 전송하는 작은 데이터 조각
  
  - 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  
  - 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

- 쿠키는 서로 다른 요청이 동일한 브라우저로부터 발생한 것인지 판단할 때 주로 사용됨
  
  - 상태가 없는(stateless) HTTP에서 상태 정보를 관리, 사용자는 로그인 상태를 유지할 수 있음

![](django_10.assets\1.PNG)

#### 쿠키 사용 목적

- 세션 관리 (Session management)
  
  - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

- 개인화 (Personalization)
  
  - 사용자 선호, 테마 등의 설정

- 트래킹 (Tracking)
  
  - 사용자 행동을 기록 및 분석

##### 세션 (Session)

- 사이트와 특정 브라우저 사이의 state(상태) 를 유지시키는 것

- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
  
  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  
  - 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 알맞은 로직을 처리

- session id 는 세션을 구별하기 위해 필요하며, 쿠키에는 session id 만 저장

#### 쿠키 Lifetime (수명)

- Session cookie
  
  - 현재 세션(current session)이 종료되면 삭제됨
  
  - 브라우저 종료와 함께 세션이 삭제됨

- Persistent cookies
  
  - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

## Login

### AuthenticationForm

- 로그인을 위한 built-in form

- 로그인 하고자 하는 사용자 정보를 입력 받음(username, password)

- ModelForm이 아닌 일반 Form을 상속 받고 있으며, request를 첫번째 인자로 취함
  ![](django_10.assets\2.PNG)

### login()

- login(request, user, backend=None)

- 인증된 사용자를 로그인
  
  - 유저의 ID를 세션에 저장하여 세션을 기록

- HttpRequest 객체와 User 객체가 필요

- 유저 정보는 반드시 인증된 유저 정보여야 함

- authenticate()함수를 활용한 인증

- AuthenticationForm을 활용한 is_valid
