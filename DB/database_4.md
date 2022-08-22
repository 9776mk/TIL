# CASE

- CASE문은 특정 상황에서 데이터를 변환하여 활용할 수 있음
- ELSE를 생략하는 경우 NULL 값이 지정됨

```sql
CASE
  WHEN 조건식 THEN 식
  WHEN 조건식 THEN 식
  ELSE 식
```

- gender가 1인 경우 남자, gender가 2인 경우 여자를 출력
  
  ```sql
  SELECT
  id,
  CASE
    WHEN gender = 1 THEN '남자'
    WHEN gender = 2 TEHN '여자'
  FROM users
  ```

- 나이에 따라 청소년(~18), 청년(~40), 중장년(~90)로 출력
  
  ```sql
  SELECT first_name, last_name,
  CASE
    WHEN age <= 18 THEN '청소년'
    WHEN age <= 40 THEN '청년'
    WHEN age <= 90 THEN '중장년'
    ELSE '노년'
  END
  FROM users
  LIMIT 10;
  ```

# 서브쿼리

- 서브 쿼리는 특정한 값을 메인 쿼리에 반환하여 활용하는 것

- 실제 테이블에 없는 기준을 이용한 검색이 가능

- 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있음

- 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음
  
  ```sql
  SELECT *
  FROM 테이블
  WHERE 컬럼1 = ()
  SELECT 컬럼1
  FROM 테이블
  );
  ```

## 단일행 서브쿼리

- 서브쿼리의 결과가 0 또는 1개인 경우

- 단일행 비교 연산자와 함께 사용(=, <, <=, >=,>, <>)
  
  ### WHERE 에서의 활용
  
  - users에서 가장 나이가 적은 사람의 수는?
    
    ```sql
    -- 가장 적은 나이
    SELECT MIN(age)
    FROM users
    -- +
    -- 나이를 세는 쿼리문
    SELECT COUNT(*)
    FROM users
    WHERE age
    -- ==
    SELECT Count(*)
    FROM users
    WHERE age = (SELECT MIN(age) FROM users);
    ```

- users에서 평균 계좌 잔고 보다 높은 사람의 수는?

```sql
-- 평균 계좌 잔고
  SELECT AVG(balance)
  FROM users;

-- 사람의 수
SELECT COUNT(*)
FROM users;

-- 평균 계좌 잔고 보다 높은 사람의 수는
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
```

- users에서 유은정과 같은 지역에 사는 사람의 수는?
  
  ```sql
  -- 유은정이 사는 지역
  SELECT country
  FROM usesrs
  WHERE first_name = '은정' AND last_name ='유'
  
  -- 지역에 사는 사람의 수
  SELECT COUNT(*)
  FROM users
  WHERE country
  
  -- 유은정과 같은 지역에 사는 사람의 수
  SELECT COUNT(*)
  FROM users
  WHERE country = (
   SELECT country
   FROM users
   WHERE first_name = '은정' AND last_name ='유'
   );
  ```

### SELECT에서 활용

- 전체 인원과 평균 잔고, 평균 나이를 출력

```sql
SELECT 
  (SELECT COUNT(*) FROM users) AS 총인원,
  (SELECT AVG(balance) FROM users) AS 평균 잔고,
  (SELECT AVG(age) FROM users) AS 평균 나이
  ;
```

### UPDATE에서 활용

```sql
-- 잔고를 전부 평균으로 바꿈
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);
```

## 다중행 서브쿼리

- 서브쿼리 결과가 2개 이상인 경우

- 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)

- user에서 이은정과 같은 지역에 사는 사람의 수는?
  
  ```sql
  SELECT COUNT(*)
  FROM users
  WHERE country = (
  SELECT country
  FROM users
  WHERE first_name = '은정' AND last_name ='이'
  );
  -- 결과 = 115
  -- 제대로 된 값이 아니다
  SELECT 
  country
  FROM country
  WHERE last_name = '이' AND first_name = '은정';
  -- country
  -- -------
  -- 전라북도
  -- 경상북도
  -- 두 지역에 있기 때문에
  SELECT country, COUNT(*)
  FROM users
  GROUP BY country;
  -- country  COUNT(*)
  -- -------  --------
  -- 강원도      101
  -- 경기도      114
  -- 경상남도     106
  -- 경상북도     103
  -- 전라남도     123
  -- 전라북도     115
  -- 제주특별자치도  118
  -- 충청남도     105
  -- 충청북도     115
  -- 전라북도의 사람들만 세어진 것을 확인할 수 있음.
  -- 행이 여러개인 다중 행인 경우인 것을 확인할 수 있음
  -- 다중행을 위한 IN을 사용할 것!
  SELECT COUNT(*)
  FROM users
  WHERE country IN (
  SELECT country
  FROM users
  WHERE first_name = '은정' AND last_name ='이'
  );
  -- COUNT(*)
  -- --------
  -- 218
  ```

## 다중칼럼 서브쿼리

- 특정 성씨에서 가장 어린 사람들의 이름과 나이

```sql
SELECT
  last_name,
  first_name,
  age
FROM users
WHERE (last_name, age) IN (
  SELECT last_name, MIN(age)
  FROM users
  GROUP BY last_name)
ORDER BY last_name;
```