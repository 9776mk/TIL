# Database
- 데이터베이스는 **체계화된 데이터의 모임**
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 

## 장점들
- 데이터 중복 최소화
- 데이터 무결성(정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성(물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지

# RDB
## 관계형 데이터베이스(RDB, Relational Database)
  - 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
  - 키(key)와 값(value)들의 간단한 관계를 표 형태로 정리한 데이터베이스

### 스키마(schema)
- 데이터에서 자료의 구조, 표현방법, 관계 등 전반적인 **명세를 기술**한 것
--- 그림 추가 ---

### 테이블(table)
- 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

#### 열
- 각 열에 고유한 데이터 형식 지정

#### 행
- 실제 데이터가 저장되는 형태

#### 기본키(Primary Key)
- 각 행(레코드)의 고유 값
- 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨
- 주민등록번호, 학번 같은 고유의 번호

# RDBMS
- 관계형 데이터베이스 관리 시스템
- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미

## SQLite
- 서버 형태가 아닌 파일 형식, 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능

# SQL
- Structured Query Language
- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리

표로 저장


# 실습
```sqlite
. database
```

## 테이블 생성 및 삭제
### CREATE

```SQL
-- classmate라는 이름의 테이블 생성
CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,
  name TEXT
);

-- 테이블 목록 조회
.tables

-- 특정 테이블 스키마 조회
.schema classamtes

-- 값 추가
INSERT INTO classmates VALUES (1, '조세호');

-- 테이블 조회
SELECT * FROM classmates;

INSERT INTO classmates VALUES (2, '이동희');

-- 테이블 삭제
DROP TABLE classmates;

```

CREATE TABLE classmates(
  name TEXT, 
  age INT, 
  address TEXT
);

.schma classamtes

### 필드 제약 조건
- NOT NULL : NULL 값 입력 금지
- UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능
- PRIMARY KEY : 테이블에서 반드시 하나, NOT NULL + UNIQUE
- FOREIGN KEY : 외래키, 다른 테이블의 Key
- CHECK : 조건으로 설정된 값만 입력 허용
- DEFAULT : 기본 설정 값

# CRUD
- Create Read Update Delete
## Create
### INSERT
- 테이블에 단일 행 삽입
```SQL
INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
```

- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력
```SQL
INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
```
--- 추가 ---
INSERT INTO classmates (name, age) VALUES ('홍길동', 23):
SELECT * FROM classmates

-- 자체적으로 아이디를 부여하고 있었음
SELECT rowid, * FROM classmates;

## READ
### SELECT
- 테이블에서 데이터를 조회
- SELECT 문은 SQLite에서 

### LIMIT

### WHERE

### SELECT DISTINCT
- 조회 결과에서 중복 행 제거

## DELETE
DELETE FROM classmates WHERE rowid=5;

## UPDATE
UPDATE classmates SET address ='서울' WHERE rowid=5                                                   
SELECT rowid, * FROM classmates;