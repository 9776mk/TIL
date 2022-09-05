[Bootstrap]([Get started with Bootstrap · Bootstrap v5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/))

## Introduction

1. index.html에 파일 생성
   
   ```html
   <!doctype html>
   <html lang="en">
   <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
   </head>
   <body>
    <h1>Hello, world!</h1>
   </body>
   </html> 
   ```

2. link는 head에, script는 body에 저장

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
```

## Layout

### Breakpoints

- breakpoints는 장치 또는 viewport크기에 맞춰 레이아웃이 작동하는 방법

- breakpoint는 반응형 설계의 기본 요소
  
  - 레이아웃을 특정 뷰포트 또는 장치 크기에 맞게 조정할 수 있는 시기를 제어하는데 사용

- 미디어 쿼리를 사용하여 중단점별로 CSS를 설계
  
  - 미디어 쿼리 : 스타일을 조건부로 적용할 수 있는 CSS의 기능

- 모바일 우선 반응형 디자인이 목표
  
  - 부트스트랩의 최소한의 스타일을 적용하여 가장 작은 중단점에서 레이아웃을 만든 후 더 큰 장치에 맞게 디자인을 조정함

#### Available breakpoints

| Breakpoint        | Class infix | Dimensions |
| ----------------- | ----------- | ---------- |
| Extra small       | None        | <576px     |
| Small             | sm          | ≥576px     |
| Medium            | md          | ≥768px     |
| Large             | lg          | ≥992px     |
| Extra large       | xl          | ≥1200px    |
| Extra extra large | xxl         | ≥1400px    |

```css
$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
);
```

#### Media queries

### Utilities