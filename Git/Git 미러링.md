1. 새로운 저장소 생성

2. 다른 개발자 저장소 clone

```bash
git clone --mirror (다른 개발자 페어 프로그래밍 저장소 주소)
cd (1에서 생성한 저장소 이름)
```

3. 복사한 저장소의 원격 저장소 설정

```bash
git remote set-url --push origin {새롭게 생성한 저장소 주소}
```

4. push

```bash
git push --mirror
```
