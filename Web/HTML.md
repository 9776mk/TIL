# HTML

- Hypertext Markup Language

- 웹 컨텐츠의 의미와 구조를 정의할 때 사용

- Hypertext : 웹 페이지를 다른 페이지로 연결하는 링크

- 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위해 "마크업" 사용
  
  - 마크업은 다양한 요소 사용
  - <head>, <title>, <body>, <header> 등등

- 요소는 태그를 사용해 문서의 다른 텍스트와 구분. 태그는 <태그 이름>로 이루어짐.
  
  - 대소문자 구분하지 않음. 

## 메인 루트

### 1. html

- HTML 문서의 루트(최상단 요소)를 나타내며, 루트 요소라고도 불림

- 모든 다른 요소는 html 요소의 후손이어야 함

```html
<!DOCTYPE html>
<html lang="ko">
  <head>...</head>
  <body>...</body>
</html>
```

## 문서 메타데이터

- 메타데이터는 스타일, 스크립트, 각종 소프트웨어의 탐색 및 렌더링을 도와줄 데이터 등 페이지에 대한 정보를 가짐

- 스타일과 스크립트 메타데이터는 페이지 안에서 정의할 수도, 다른 파일로 링크할 수도 있음

### 1. <base>

- 모든 상대 URL이 사용할 기준 URL 지정.

- 하나의 <base>요소만 존재

- href : 문서 내 상대 URL이 사용할 기준 URL. 절대 및 상대 URL을 사용할 수 있음

### 2. <head>

- 기계가 식별할 수 있는 문서 정보(메타데이터)를 담음

- 문서가 사용할 제목, 스크립트, 스타일 시트 등이 있음

```html
<!doctype html>
<html>
  <head>
    <title>문서 제목</title>
  </head>
</html>
```

### 3. <link>

- 현재 문서와 외부 리소스의 관계 명시

- 스타일 시트를 연결할 때 가장 많이 사용됨
  
  ```html
  <link href="main.css" rel="stylesheet">
  ```

### 4. <meta>

- 문서 레벨 메타데이터 요소

- 다른 메타관련 요소로 나타낼 수 없는 메타데이터를 나타냄.

#### 특성

- charset : 페이지의 문자 인코딩 선언

- content : http-equiv 또는 name의 특성값

- http-equiv : 프래그마 지시문 정의.

- name : name과 content 특성을 함께 사용하여 문서의 메타데이터를 이름-값 쌍으로 제공 가능

```html
<meta charset="utf-8">

<!-- 3초 후 리다이렉트 -->
<meta http-equiv="refresh" content="3;url=https://www.mozilla.org">
```

### 5. <style>

- 스타일 정보 요소

- 문서나 문서 일부에 대한 스타일 정보를 포함.

- \<style\>요소는 문서의 <head>안에 위치해야 하나, 일반적으로 외부 스타일 시트에 작성하고, <link> 요소로 연결하는 편이 좋음.

- 다수의 <style>과 <link> 요소를 포함하면 서로의 순서대로 DOM에 스타일을 적용하기 때문에 올바른 순서에 따라 요소들을 배치.

```html
<!doctype html>
<html>
<head>
  <style>
    p {
      color: white;
      background-color: blue;
      padding: 5px;
      border: 1px solid black;
    }
  </style>
  <style>
    p {
      color: blue;
      background-color: yellow;
    }
  </style>
</head>
<body>
  <p>This is my paragraph.</p>
</body>
</html>
```

- 같은 이름일 경우 뒤쪽 style이 앞쪽을 덮어 씀

### 6. <title> : 문서 제목 요소

- 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의

- 텍스트만 포함할 수 있으며 태그를 포함하더라도 무시

```html
<title>엄청 흥미로운 내용</title>
```

## 구획 루트

### <body>

- HTML 문서의 내용을 나타냄

- 한 문서에 하나의 <body> 요소만 존재
  
  - alink : 선택한 하이

```html
<html>
  <head>
    <title>문서 제목</title>
  </head>
  <body>
    <p>문단입니다</p>
  </body>
</html>
```

## 콘텐츠 구획

- 콘텐츠 구획 요소를 사용하여 문서의 콘텐츠를 논리적인 조각으로 체계화할 수 있음

### 1. <address>

- 가까운 HTML 요소의 사람, 단체, 조직 등에 대한 연락처 정보

- 어떠한 정보라도 포함될 수 있음

- 연락처가 가리키는 개인, 조직, 단체의 이름은 반드시 포함

```html
<address>
  You can contact author at <a href="http://www.somedomain.com/contact">
  www.somedomain.com</a>.<br>
  If you see any bugs, please <a href="mailto:webmaster@somedomain.com">
  contact webmaster</a>.<br>
  You may also want to visit us:<br>
  Mozilla Foundation<br>
  331 E Evelyn Ave<br>
  Mountain View, CA 94041<br>
  USA
</address>
```

- 겉보기는 <i>나 <em>요소와 같지만, 자체적인 의미를 갖고 있으므로 연락처 표기에는 address 사용

### 2. <article>

- 문서, 페이지, 애플리케이션, 또는 사이트 안에서 독립적으로 구분해 배포하거나 재사용할 수 있는 구획

- 게시판, 블로그 글, 매거진, 뉴스 기사 등이 해당

- 각각의 <article>을 식별할 수단이 필요. 주로 제목(<h1> - <h6>) 요소를 <article>의 자식으로 포함하는 방법 사용

- <article> 요소가 중첩되어 있을 때, 안쪽에 있는 요소는 바깥쪽에 있는 요소와 관련된 글을 나타냄.
  
  - 글과 댓글은 글의 <article>안에 중첩한 <aricle>로 표현 가능

- <article> 요소의 작성자 정보를 <address>요소로 제공가능하나, 중첩 <article>에는 적용되지 않음.

```html
<article class="film_review">
  <header>
    <h2>Jurassic Park</h2>
  </header>
  <section class="main_review">
    <p>Dinos were great!</p>
  </section>
  <section class="user_reviews">
    <article class="user_review">
      <p>Way too scary for me.</p>
      <footer>
        <p>
          Posted on <time datetime="2015-05-16 19:00">May 16</time> by Lisa.
        </p>
      </footer>
    </article>
    <article class="user_review">
      <p>I agree, dinos are my favorite.</p>
      <footer>
        <p>
          Posted on <time datetime="2015-05-17 19:00">May 17</time> by Tom.
        </p>
      </footer>
    </article>
  </section>
  <footer>
    <p>
      Posted on <time datetime="2015-05-15 19:00">May 15</time> by Staff.
    </p>
  </footer>
</article>
```

### 3. <aside>

- 문서의 주요 내용과 간접적으로만 연관된 부분을 나타냄

- 주로 사이드바 혹은 콜아웃 박스로 표현

```html
<article>
  <p>
    디즈니 만화영화 <em>인어 공주</em>는
    1989년 처음 개봉했습니다.
  </p>
  <aside>
    인어 공주는 첫 개봉 당시 8700만불의 흥행을 기록했습니다.
  </aside>
  <p>
    영화에 대한 정보...
  </p>
</article>
```

### 4. <footer>

- 가장 가까운 구획 콘텐츠나 구획 루트의 푸터를 나타냄.
  
  - 일반적으로 구획의 작성자, 저작권 정보, 관련 문서 등의 내용을 담음

- <address>  요소로 감싼 작성자 정보를 <footer>에 배치

```html
<footer>
  Some copyright info or perhaps some author
  info for an <article>?
</footer>
```

### 5. <header>

- 소개 및 탐색에 도움을 주는 콘텐츠

- 제목, 로고, 검색 폼, 작성자 이름 등의 요소도 포함 가능

- 구획 콘텐츠가 아니므로 개요에 구획을 생성하지 않음.

- 페이지 제목
  
  ```html
  <header>
  <h1>Main Page Title</h1>
  <img src="mdn-logo-sm.png" alt="MDN logo">
  </header>
  ```

- 글 제목
  
  ```html
  <article>
  <header>
    <h2>The Planet Earth</h2>
    <p>Posted on Wednesday, <time datetime="2017-10-04">4 October 2017</time> by Jane Smith</p>
  </header>
  <p>We live on a planet that's blue and green, with so many things still unseen.</p>
  <p><a href="https://janesmith.com/the-planet-earth/">Continue reading....</a></p>
  </article>
  ```

### 6. <h1>,<h2>,<h3>,<h4>,<h5>,<h6>

- 6단계의 구획 제목을 나타냄

- 구획 단계는 <h1>이 가장 높고 <h6>이 가장 낮음

- 글씨 크기를 위해서는 CSS의 font-size를 사용할 것

- 제목 단계 건너뛰지 않기. <h1>에서, <h2>, ... 순차적으로 기입할 것

```html
<h1>Heading elements</h1>
<h2>Summary</h2>
<p>Some text here...</p>

<h2>Examples</h2>
<h3>Example 1</h3>
<p>Some text here...</p>

<h3>Example 2</h3>
<p>Some text here...</p>

<h2>See also</h2>
<p>Some text here...</p>
```

### 7. <main>

- <body>의 주요 콘텐츠를 나타냄.

- 주요 콘텐츠 영역은 문서의 핵심 주제나 앱의 핵심 기능에 직접적으로 연결됐거나 확장하는 콘텐츠로 이루어짐

- <main>은 문서의 유일한 내용이어야 함

- 요소 개요에 영향을 주지 않음. 페이지의 개념적 구조를 바꾸지 않으며 온전히 정보 제공용

```html
<!-- other content -->

<main>
  <h1>Apples</h1>
  <p>The apple is the pomaceous fruit of the apple tree.</p>

  <article>
    <h2>Red Delicious</h2>
    <p>These bright red apples are the most common found in many
    supermarkets.</p>
    <p>... </p>
    <p>... </p>
  </article>

  <article>
    <h2>Granny Smith</h2>
    <p>These juicy, green apples make a great filling for
    apple pies.</p>
    <p>... </p>
    <p>... </p>
  </article>

</main>

<!-- other content -->
```

- 건너뛰기 링크 : 건너뛰기 링크는 반복되는 큰 구획을 빠르게 넘어갈 수 있는 기법
  
  - 사용자가 페이지의 주요 내용으로 신속하게 접근할 수 있도록 도와줌
  
  - <main> 요소에  id 요소를 추가해 건너뛰기 링크의 대상으로 지정됨

```html
<body>
  <a href="#main-content">Skip to main content</a>

  <!-- navigation and header content -->

  <main id="main-content">
    <!-- main page content -->
  </main>
</body>
```

### 8. <nav>

- 문서의 부분 중 현재 페이지 내, 또는 다른 페이지로의 링크를 보여주는 구획

- 메뉴, 목차, 색인 등

-  <nav> 요소는 주요 탐색 링크 블록을 위한 요소

- 보통 <footer> 요소가 <nav>에 들어가지 않아도 되는 링크를 포함

- <nav> 하나는 사이트 전체 탐색, 다른 하나는 현재 페이지 내 탐색으로 사용하는 등, 하나의 문서에서 여러 개의 <nav> 태그를 가질 수 있음

- 스크린 리더 등 장애를 가진 사용자를 위한 에이전트는 최초 렌더링에서 탐색 전용 콘텐츠를 제외할지 결정할 때 <nav>를 참고

```html
<nav>
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

### 9. <section>

- HTML 문서의 독립적인 구획을 나타내며, 더 적합한 의미를 가진 요소가 없을 때 사용

- 주로 제목<h1> <h6>요소를 <section>의 자식으로 포함하는 방법을 사용해 각각의 <section>을 식별

```html
<div>
  <h2>Heading</h2>
  <img>some image</img>
</div>
```

## 텍스트 콘텐츠

- HTML 텍스트 콘텐츠를 사용하여 <body> 태그 사이의 블록이나 콘텐츠 구획을 정리

### 1. <blockquote>

- 인용 블록 요소

- 안쪽의 텍스트가 긴 인용문을 나타내며, 주로 들여쓰기를 한 것으로 그려짐

- cite : 인용문의 출처 문서나 메시지를 가리키는 URL

- 들여쓰기를 바꾸려면  CSS margin-left와 margin-right을 사용

- 별도의 블록을 쓰지 않아도 될 짧은 인용문은 <q> 요소 사용

```html
<blockquote cite="https://tools.ietf.org/html/rfc1149">
  <p>Avian carriers can provide high delay, low
  throughput, and low altitude service.  The
  connection topology is limited to a single
  point-to-point path for each carrier, used with
  standard carriers, but many carriers can be used
  without significant interference with each other,
  outside of early spring.  This is because of the 3D
  ether space available to the carriers, in contrast
  to the 1D ether used by IEEE802.3.  The carriers
  have an intrinsic collision avoidance system, which
  increases availability.</p>
</blockquote>
```

### 2. <div>

- 콘텐츠 분할 요소

- 플로우 콘텐츠를 위한 통용 컨테이너

- CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않음.

- <div> 요소는 순수 컨테이너로서 아무것도 표현하지 않음

- 다른 요소 여럿을 묶어 class 나 id 속성으로 꾸미기 쉽도록 돕거나, 문서의 특정 구역이 다른 언어임을 표시(lang 속성 사용)하는 등의 용도로 사용 가능

- <article>, <nav> 등 의미를 가진 다른 요소가 적절하지 않을 때만 사용해야 함

```html
<div>
   <p>어떤 콘텐츠든 좋습니다.
   <p>, <table>같이 말이죠. 써보세요!</p>
</div>
```

HTML

```html
<div class="shadowbox">
  <p>Here's a very interesting note displayed in a
  lovely shadowed box.</p>
</div>
```

```css
.shadowbox {
  width: 15em;
  border: 1px solid #333;
  box-shadow: 8px 8px 5px #444;
  padding: 8px 12px;
  background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc);
}
```

### 3. <dl>

- <dl>은 <dt>로 표기한 용어와 <dd> 요소로 표기한 설명 그룹의 목록을 감싸서 설명 목록을 생성
- 주로 용어사전 구현이나 메타데이터(키-값 쌍 목록)를 표시할 때 사용
- 하나의 용어와 하나의 정의

```html
<dl>
  <dt>Firefox</dt>
  <dd>
    Mozilla 재단과 수 백명의
    자원봉사자가 개발한 무료
    오픈소스 크로스 플랫폼
    그래픽 웹 브라우저.
  </dd>

  <!-- 다른 용어 및 정의 -->
</dl>
```

- 여러 개의 용어와 하나의 정의

```html
<dl>
  <dt>Firefox</dt>
  <dt>Mozilla Firefox</dt>
  <dt>Fx</dt>
  <dd>
    Mozilla 재단과 수 백명의
    자원봉사자가 개발한 무료
    오픈소스 크로스 플랫폼
    그래픽 웹 브라우저.
  </dd>

  <!-- 다른 용어 및 정의 -->
</dl>
```

- 하나의 용어와 여러 개의 정의

```html
<dl>
  <dt>Firefox</dt>
  <dd>
    Mozilla 재단과 수 백명의
    자원봉사자가 개발한 무료
    오픈소스 크로스 플랫폼
    그래픽 웹 브라우저.
  </dd>
  <dd>
    붉은 판다, 레서 판다, 랫서 판다,
    혹은 "Firefox"는 초식성 포유류이다.
    몸 길이는 애완용 고양이보다 약간
    큰 정도인 60cm다.
  </dd>

  <!-- 다른 용어 및 정의 -->
</dl>
```

- 메타데이터
  
  - 키-값 쌍으로 표시할 때도 유용함

```html
<dl>
  <dt>Name</dt>
  <dd>Godzilla</dd>
  <dt>Born</dt>
  <dd>1952</dd>
  <dt>Birthplace</dt>
  <dd>Japan</dd>
  <dt>Color</dt>
  <dd>Green</dd>
</dl>
```

### 4. <figure>

- 독립적인 콘텐츠를 표현

- 처음이나 마지막 자식으로 <figcaption>을 넣어서 설명을 붙일 수 있음

```html
<figure>
  <figcaption><code>navigator</code>를 이용하여 브라우저 정보 얻기</figcaption>
  <pre>
function NavigatorExample() {
  var txt;
  txt = "Browser CodeName: " + navigator.appCodeName;
  txt+= "Browser Name: " + navigator.appName;
  txt+= "Browser Version: " + navigator.appVersion ;
  txt+= "Cookies Enabled: " + navigator.cookieEnabled;
  txt+= "Platform: " + navigator.platform;
  txt+= "User-agent header: " + navigator.userAgent;
}
  </pre>
</figure>
```

### 5. <hr>

- 이야기 장면 전환, 구획 내 주제 변경 등, 문단 레벨 요소에서 주제의 분리를 나타냄

- 역사적으로 <hr>은 가로줄로 표현했지만, 의미를 가지게 됨

- 따라서 가로줄을 그리고 싶다면 적절한 CSS를 사용해야 함

```html
<p>
This is the first paragraph of text.
This is the first paragraph of text.
This is the first paragraph of text.
This is the first paragraph of text.
</p>

<hr>

<p>
This is second paragraph of text.
This is second paragraph of text.
This is second paragraph of text.
This is second paragraph of text.
</p>
```

### 6. <p>, <pre>

- \<p\>는 하나의 문단을 나타냄.

```html
<p>첫 번째 문단입니다.
  첫 번째 문단입니다.
  첫 번째 문단입니다.
  첫 번째 문단입니다.</p>
<p>두 번째 문단입니다.
  두 번째 문단입니다.
  두 번째 문단입니다.
  두 번째 문단입니다.</p>
```

- \<pre\> 는 미리 서식을 지정한 텍스트를 나타내며, HTML에 작성한 내용 그대로 표현

```html
<p>CSS로 글자 색을 바꾸는건 쉽습니다.</p>
<pre>
body {
  color:red;
}
</pre>
```

```html
<figure role="img" aria-labelledby="cow-caption">
  <pre>
  _______________________
< 나는 이 분야의 전문가다. >
  -----------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
  </pre>
  <figcaption id="cow-caption">
    소 한 마리가 "나는 이 분야의 전문가다"라고 말하고 있습니다. 소는 미리 서식을 적용한 텍스트로 그려져있습니다.
  </figcaption>
</figure>
```

- \<figure\>과 \<figcaption\>에 더해 id와 ARIA role과 aria-labelledby 특성을 조합하면 <pre>를 마치 이미지처럼 표현하면서 <figcaption>을 대체 설명으로 사용할 수 있음

### 7. <menu>

- 사용자가 수행하거나 하는 명령 묶음

- label : 사용자에게 보여지는 메뉴의 이름

```html
<!-- A button, which displays a menu when clicked. -->
<button type="menu" menu="dropdown-menu">
  Dropdown
</button>

<menu type="context" id="dropdown-menu">
  <menuitem label="Action">
  <menuitem label="Another action">
  <hr>
  <menuitem label="Separated action">
</menu>
```

### 8. <ol>, <ul>, <li>

- \<ol\> : 정렬된 목록. 보통 숫자 목록으로 표현
  
  - reversed : 역순으로 배열 할지
  
  - start : 항목을 셀 때 시작할 수. 4부터 세고 싶으면 start="4"
  
  - type : 항목을 셀 때 사용할 카운터 유형
    
    - 'a'는 소문자 알파벳
    
    - 'A'는 대문자 알파벳
    
    - 'i'는 소문자 로마 숫자
    
    - 'I'는 대문자 로마 숫자
    
    - '1'은 숫자(기본값)

- 간단한 예제

```html
<ol>
  <li>first item</li>
  <li>second item</li>
  <li>third item</li>
</ol>
```

- 로마 숫자로 표기

```html
<ol type="i">
  <li>Introduction</li>
  <li>List of Greivances</li>
  <li>Conclusion</li>
</ol> 
```

- start 특성 사용

```html
<p>Finishing places of contestants not in the winners’ circle:</p>

<ol start="4">
  <li>Speedwalk Stu</li>
  <li>Saunterin’ Sam</li>
  <li>Slowpoke Rodriguez</li>
</ol>
```

- 중첩 목록

```html
<ol>
  <li>first item</li>
  <li>second item  <!-- closing </li> tag not here! -->
    <ol>
      <li>second item first subitem</li>
      <li>second item second subitem</li>
      <li>second item third subitem</li>
    </ol>
  </li>            <!-- Here's the closing </li> tag -->
  <li>third item</li>
</ol>
```

- 정렬 안의 비정렬 목록

```html
<ol>
  <li>first item</li>
  <li>second item      <!-- Look, the closing </li> tag is not placed here! -->
    <ul>
      <li>second item first subitem</li>
      <li>second item second subitem</li>
      <li>second item third subitem</li>
    </ul>
  </li>                <!-- Here is the closing </li> tag -->
  <li>third item</li>
</ol>
```

- <ul> : 요소는 정렬되지 않은 목록. 보통 불릿으로 표현

- 간단한 예제

```html
<ul>
  <li>first item</li>
  <li>second item</li>
  <li>third item</li>
</ul>
```

- 중첩 목록

```html
<ul>
  <li>first item</li>
  <li>second item
  <!-- Look, the closing </li> tag is not placed here! -->
    <ul>
      <li>second item first subitem</li>
      <li>second item second subitem
      <!-- Same for the second nested unordered list! -->
        <ul>
          <li>second item second subitem first sub-subitem</li>
          <li>second item second subitem second sub-subitem</li>
          <li>second item second subitem third sub-subitem</li>
        </ul>
      </li> <!-- Closing </li> tag for the li that
                  contains the third unordered list -->
      <li>second item third subitem</li>
    </ul>
  <!-- Here is the closing </li> tag -->
  </li>
  <li>third item</li>
</ul>
```

- 비정렬 안의 정렬 목록

```html
<ul>
  <li>first item</li>
  <li>second item
  <!-- Look, the closing </li> tag is not placed here! -->
    <ol>
      <li>second item first subitem</li>
      <li>second item second subitem</li>
      <li>second item third subitem</li>
    </ol>
  <!-- Here is the closing </li> tag -->
  </li>
  <li>third item</li>
</ul>
```

- \<li\> : 목록의 항목. 반드시 정렬 목록, 비정렬 목록, 메뉴 안에 위치해야 함
  
  - 메뉴와 비정렬 목록에서는 불릿, 정렬 목록에서는 숫자나 문자를 사용한 오름차순 카운터

- 정렬 목록

```html
<ol>
    <li>first item</li>
    <li>second item</li>
    <li>third item</li>
</ol>
```

- 사용자 지정 값을 가진 정렬 목록

```html
<ol type="I">
    <li value="3">third item</li>
    <li>fourth item</li>
    <li>fifth item</li>
</ol>
```

- 비정렬 목록

```html
<ul>
    <li>first item</li>
    <li>second item</li>
    <li>third item</li>
</ul>
```

## 인라인 텍스트 시멘틱

- HTML 인라인 텍스트 시멘틱을 사용해서 단어, 줄, 혹은 아무 부분의 의미나 구조, 스타일을 정의할 수 있음

### 1. <a>

- 앵커 요소는 href 특성을 통해 다른 페이지나 같은 페이지의 어느 위치, 파일, 이메일 주소와 그 외 다른 URL로 연결할 수 있는 하이퍼링크를 만듦

-  <a> 안의 콘텐츠는 링크 목적지의 설명을 나타내야 함

- href : 하이퍼링크가 가리키는 URL

- 절대 URL로 연결

```html
<a href="https://www.mozilla.com">
  Mozilla
</a>
```

- 상대 URL로 연결

```html
<a href="//example.com">Scheme-relative URL</a>
<a href="/en-US/docs/Web/HTML">Origin-relative URL</a>
<a href="./p">Directory-relative URL</a>
```

- 같은 페이지의 요소로 연결
  
  ```html
  <!-- <a> 요소로 아래의 구획에 연결 -->
  <p><a href="#Section_further_down">
  아래 제목으로 건너뛰기
  </a></p>
  <!-- 링크가 향할 제목 -->
  <h2 id="Section_further_down">아래의 제목</h2>
  ```

- 건너뛰기 링크
  
  - <body> 콘텐츠에서 가능함. 앞쪽에 배치하는 링크로 페이지의 주요 콘텐츠 시작 점을 가리킴.
    
    ```html
    <body>
    <a href="#content">내용으로 건너뛰기</a> 
    <header>
    …
    </header>
    <main id="content"> <!-- 여기로 건너뜀 -->
    ```

### 2. <abbr>

- 준말 또는 머리 글자

- 선택 속성인 title 사용 시 준말의 전체 뜻이나 설명 제공 가능

- 준말임을 나타내기
  
  - 설명 없이, 단순히 특정 단어가 준말임을 나타내기
    
    ```html
    <p>Using <abbr>HTML</abbr> is fun and easy!</p>
    ```

- 펼친 형태 보여주기
  
  - title 특성을 사용하여 준말과 머리글자를 펼친 원래 형태를 보여줄 수 있음
    
    ```html
    <p>Ashok's joke made me <abbr title="Laugh Out Loud">LOL</abbr> big
    time.</p>
    ```

- 준말 정의
  
  - <abbr>과 <dfn>을 사용하면 준말을 정식으로 정의 가능
    
    ```html
    <p><dfn id="html"><abbr title="HyperText Markup Language">HTML</abbr>
    </dfn> is a markup language used to create the semantics and structure
    of a web page.</p>
    <p>A <dfn id="spec">Specification</dfn>
    (<abbr title="Specification">spec</abbr>) is a document that outlines in detail     how a technology or API is intended to function and how it is accessed.</p>
    ```

### 3. <b>

- 독자의 주의를 요소의 콘텐츠로 끌기 위한 용도로 사용

- 굵은 글씨체로 사용할 경우 CSS font-weight의 "bold"나 <strong> 요소를 사용
  
  - <strong> : 중요한 글
  
  - <em> : 약간의 강조가 필요한 글
    
    - 주로 기울임꼴로 표현됨. 기울임이 필요하기 위해서는 CSS font-sytle (en_US)
      
      ```html
      <p>
      과거에 <em>block-level</em>이라 불렸던
      콘텐츠는 HTML 5부터 <em>flow</em> 콘텐츠라고
      말합니다.
      </p>
      ```
    
    - 다른 기울임 꼴
      
      - <cite> : 저작물(책, 연극, 음악 등등)의 제목
        
        ```html
        <p>More information can be found in <cite>[ISO-0000]</cite>.</p>
        ```
      
      - <i> : 학명 등 과학적인 이름, 다른 언어의 단어 등, 주변과 다른 톤을 가진 텍스트
  
  - <mark> : 관련성이 있는 글

```html
<p>
  This article describes several <b class="keywords">text-level</b> elements.
  It explains their usage in an <b class="keywords">HTML</b> document.
</p>
Keywords are displayed with the default style of the <b>element, likely in bold</b>.
```

### 4. <br>

- 텍스트 안에 줄바꿈을 생성

- 주소나 시조 등 줄의 구분이 중요한 내용을 작성할 때 사용

- 줄 간격을 늘리기 위해서는 CSS line-height_(en-US) 속성 사용
  
  ```html
  Mozilla Foundation<br>
  1981 Landings Drive<br>
  Building K<br>
  Mountain View, CA 94043-0801<br>
  USA
  ```

### 5. <q>

- 둘러싼 텍스트가 짧은 인용문

- 줄 바꿈이 없는 짧은 경우에 적합

- 긴 인용문은 <blockquote>

```html
<p>Mozilla 재단의 웹사이트에 따르면,
  <q
  cite="https://www.mozilla.org/en-US/about/history/details/">Firefox 1.0
  은 2004년 처음 공개되어 큰 성공을 거두었습니다.</q></p>
```

### 6. <s>
- 글자에 취소선, 즉 글자를 가로지르는 선을 그림
```html
<s>Today's Special: Salmon</s> SOLD OUT<br>
```

### 7. <span>
- 아무 뜻이 없음
- 스타일 혹은 어떤 특성의 값을 서로 공유하는 요소로 묶을 때 사용가능
- <div>는 블록 레벨 요소, <span>은 인라인 요소
```html
<p><span>Some text</span></p>
```

## 이미지 & 멀티미디어
- HTML은 사진, 오디오, 비디오 등 다양한 멀티미디어 리소스를 지원
### 1. <map>
- <area> 요소와 함께 이미지 맵(클릭 가능한 링크 영역)을 정의할 때 사용
- name : 맵을 참조할 때 사용할 수 있는 이름
	- 반드시 존재, 공백 문자 포함하면 안됨, 모든 <map>에서 유일, id 특성이 존재한 경우 name과 값이 동일해야 함
    
```html
<map name="primary">
  <area shape="circle" coords="75,75,75" href="left.html">
  <area shape="circle" coords="275,75,75" href="right.html">
</map>
<img usemap="#primary" src="https://placehold.it/350x150" alt="350 x 150 pic">
```
    
### 2. <area>
- 이미지의 핫스팟 영역을 정의하고, 하이퍼링크를 추가할 수 있음
- <map>요소 안에서만 사용할 수 있음
	- shape : 핫스팟의 모양. rect, circle, poly
    - coords : 핫스팟 영역을 지정하는 일련의 좌표. 값의 수와 의미는 shape 특성에 따라 달라짐
    - href : <area>의 하이퍼링크 대상. 생략할 경우 하이퍼링크를 나타내지 않음.
    - alt : 이미지를 출력하지 않는 브라우저에서 대신 표시할 대안 텍스트. href 특성이 존재할 경우 필수

```html
<map name="primary">
  <area shape="circle" coords="200,250,25" href="another.htm" />
  <area shape="default" nohref />
</map>
<img usemap="#primary" src="http://placehold.it/350x150" alt="350 x 150 pic">
```


### 3. <img>, <audio>, <video>
- 이미지, 오디오, 비디오 파일 삽입
```html
<a href="https://developer.mozilla.org">
     <img src="favicon144.png" alt="Visit the MDN site">
   </a>
```
```html
<!-- Simple audio playback -->
<audio
  src="AudioTest.ogg"
  autoplay>
  Your browser does not support the <code>audio</code> element.
</audio>
```
```html
<!-- Simple video example -->
<video src="videofile.ogg" autoplay poster="posterimage.jpg">
  Sorry, your browser doesn't support embedded videos,
  but don't worry, you can <a href="videofile.ogg">download it</a>
  and watch it with your favorite video player!
</video>

<!-- Video with subtitles -->
<video src="foo.ogg">
  <track kind="subtitles" src="foo.en.vtt" srclang="en" label="English">
  <track kind="subtitles" src="foo.sv.vtt" srclang="sv" label="Svenska">
</video>
```