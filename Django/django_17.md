# AJAX

## Asynchronous JavaScript

### 비동기식

- 병렬적 Task 수행

- 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐(non-blocking)

- 요청을 보내고 응답을 기다리지 않고 다음 코드가 실행됨

- JavaScript는 single threaded 방식이기 때문에 기다려주지 않음

### Event Loop 기반 동시성 모델

- Call Stack
  
  - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 stack(LIFO) 형태의 자료구조

- Web API(Browser API)
  
  - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
  
  - 예) setTimeout(), AJAX

### AJAX

- Asynchronous JavaScript And ~~XML~~ HTML(비동기식 JavaScript와 XML 요즘은 JASON)

- 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부부만 업데이트 가능

- 비동기 통신 웹 개발 기술이 AJAX

- 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios



### Axios

- "Promise based HTTP client for the browser and Node.js"
  
  - 도착하면 실행을 시켜주겠다는 약속

- 브라우저를 위한 Promise 기반의 클라이언트
