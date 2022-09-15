# JavaScript

- 웹 페이지에서 복잡한 기능을 구현할 수 있도록 하는 스크립팅 언어 또는 프로그래밍 언어

![](JavaScrpit.assets/1.png)

- 표준 웹 기술
  
  - HTML : 웹 구조를 짜고 의미를 부여하는 마크업 언어
  
  - CSS : HTML 콘텐츠에 스타일을 적용할 수 있는 스타일 규칙 언어
  
  - JavaScript : 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어, 애니메이션 등을 추가하는 스크립팅 언어

- 예시

```html
<p>Player 1: Chris</p>
```

```css
p {
  font-family: 'helvetica neue', helvetica, sans-serif;
  letter-spacing: 1px;
  text-transform: uppercase;
  text-align: center;
  border: 2px solid rgba(0, 0, 200, 0.6);
  background: rgba(0, 0, 200, 0.3);
  color: rgba(0, 0, 200, 0.6);
  box-shadow: 1px 1px 2px rgba(0, 0, 200, 0.4);
  border-radius: 10px;
  padding: 3px 10px;
  display: inline-block;
  cursor: pointer;
}
```

```javascript
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

## JavaScript 기능

- 변수에 값을 저장

- 텍스트 조각을 저장

- 웹 페이지에서 발생하는 어떤 이벤트에 코드가 응답하도록 함

- API(Application Programming Interface)
  
  - 개발자가 직접 구현하기는 어렵거나 불가능한 기능들을 미리 만들어서 제공
    ![](JavaScrpit.assets/2.png)
    
    1. 브라우저 API
       
       - 웹 브라우저에 내장된  API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행
       
       - DOM(Document Object Model) API : HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작
       
       - Geolocation API : 지리정보
       
       - Canvas, WebGL API : 애니메이션을 적용한 2D와 3D 그래픽
    
    2. 서드파티 API 
       
       - 브라우저에 탑재되지 않은 API로, 웹의 어딘가에서 직접 코드와 정보를 찾아야 함
       
       - Twitter API, Google 지도 API, OpenStreetMap API 등

## JavaScript 실행 순서

- 일반적으로 위에서 아래로 순서대로 실행

```javascript
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

## 웹 페이지에 JavaScript 넣기

### 내부 JavaScript

1. <script> \</script> 안에 작성

### 외부 JavaScript

1. HTML 파일과 같은 폴더에 새로운 파일을 만들기

2. script.js 로 이름 붙이기

3. \<script> 요소 대신 아래의 코드 작성

```javascript
<script src="script.js" defer></script>
```

4. script.js 파일 안에 아래 내용 입력

```javascript
function createParagraph() {
  const para = document.createElement('p');
  para.textContent = 'You clicked the button!';
  document.body.appendChild(para);
}

const buttons = document.querySelectorAll('button');

for (const button of buttons) {
  button.addEventListener('click', createParagraph);
}
```

### 스크립트 위치 주의 사항!

- 일반적으로 위에서 아래로 진행

- HTML 읽기 - HTML 파싱 - DOM 트리 생성 - Render 트리 생성 - Display 표시 순으로 웹 브라우저가 웹 문서를 읽음

- \<script> 태그를 만나면 파싱이 시작되게 됨

- HTML 코드보다 JavaScript를 먼저 불러오므로 문제가 발생할 수 있음

- 예방 방법
1. 내부 예제. HTML 본문 전체를 불러와 읽었다는 것을 나타내는 이벤트를 활용

```javascript
document.addEventListener('DOMContentLoaded', () => {
  ...
});
```

2. 외부 예제. defer는 브라우저가 \<script> 태그를 마주쳐도 그 이후의 HTML 콘텐츠를 계쏙 불러오도록 지정

```javascript
<script src="script.js" defer></script>
```

- 스크립트 요소를 본문의 맨 마지막(\</body> 태그 앞)에 배치
  
  - 모든 HTML을 읽은 후에 스크립트를 불러옴
    
    - HTML DOM을 모두 불러오기 전에는 스크립트의 로딩과 분석이 완전히 중단됨
    - 많은 스크립트를 포함하는 대형 사이트에서는 성능이 저하될 수 있음

## 문법과 자료형

### 기본

- 대소문자 구별, 유니코드 문자셋 이용

```javascript
var 갑을 = "병정";
var abc = "def";
```

### 주석

```javascript
// 주석주석

/*
주석
주우우우우
서어어억
*/
```

### 선언

- var : 변수를 선언, 추가로 동시에 값을 초기화

- let : 블록 스코프 지역 변수를 선언, 추가로 동시에 값을 초기화

- const : 블록 스코프 읽기 전용 상수를 선언

### 변수

- 문자, 밑줄(_), 달러기호($)로 시작해야 함.

- 대소문자 구분

#### 1. 변수 선언

1. var x = 42 
   
   - var 키워드로 변수 선언
   
   - 지역 및 전역 변수 선언에 사용

2. let y = 13
   
   - const 혹은 let 키워드로 변수 선언
   
   - 블록 스코프 지역 변수 선언

#### 2. 변수 할당

- 지정된 값 없이 var 혹은 let 문을 사용해서 선언된 변수는 undefined 값을 가짐

- 선언되지 않은 변수에 접근을 시도하면 ReferenceErro 예외 발생

```javascript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;
// 변수 호이스팅을 배워서 이해할 

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```

- undefined 값 활용

```javascript
// input 변수에 값 할당x -> undefined
var input;
if(input === undefined) {
  doThis();
} else {
  doThat();
}

// boolean에서는 false로 동작
var myArray = [];
if (!myArray[0]) myFunction();

// 수치 맥락에선 NaN
var a;
a + 2; // NaN으로 평가

// null 값을 평가할 때, 수치 맥락에서는 0으로, boolean에서는 false로 동작
var n = null;
console.log(n * 32); // 콘솔에 0 으로 로그가 남음
```

#### 3. 변수 스코프

- 전역 변수 : 어떤 함수의 바깥에 변수를 선언하여 현재 문서의 다른 코드에 해당 변수를 사용할 수 있음

- 지역 변수 : 함수 내부에 변수를 선언해서 오직 그 함수 내에서만 사용할 수 있음

```javascript
if (true) {
  var x = 5;
}
console.log(x); // 5

if (true) {
  let y = 5;
}
console.log(y); // ReferenceError: y is not defined
```

#### 4. 변수 호이스팅

-  JavaScript 변수가 어떤 의미에서 함수나 문의 최상단으로 "올려지는" 것

- 나중에 선언된 변수를 참조할 수 있음

- 끌어올려진 변수는 `undefined` 값을 반환 -> 사용 혹은 참조한 후에 선언 및 초기화하더라도 여전히 undefined를 반환

#### 5. 전역 변수

- 전역 변수는 전역 객체의 속성

- 웹 페이지에서 전역 객체는 window이므로, `windows.variable` 구문을 통해 전역 변수를 설정하고 접근할 수 있음

### 상수

- const 키워드로 읽기 전용 상수를 만들 수 있음

- 문자, 밑줄이나 달러 기호($)로 시작해야 하고, 문자, 숫자나 밑줄을 포함할 수 있음

```javascript
const PI = 3.14;
```

- 상수는 스크립트가 실행 중인 동안 대입을 통해 값을 바꾸거나 재선언될 수 없고, 값으로 초기화해야 함

```javascript
// 같은 스코프에 있는 함수나 변수와 동일한 이름으로 선언할 수 없음
// 오류가 발생합니다
function f() {};
const f = 5;

// 역시 오류가 발생합니다
function f() {
  const g = 5;
  var g;

  //statements

  // 상수에 할당된 객체의 속성은 보호되지 않음
  const MY_OBJECT = {'key': 'value'};
  MY_OBJECT.key = 'otherValue';

  // 배열의 내용도 보호되지 않음
  const MY_ARRAY = ['HTML','CSS'];
  MY_ARRAY.push('JAVASCRIPT');
  console.log(MY_ARRAY); //logs ['HTML','CSS','JAVASCRIPT'];
}
```



### 데이터 구조 및 형

1. Boolean

2. null

3. undefined

4. 