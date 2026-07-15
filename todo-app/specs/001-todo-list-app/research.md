# 연구 노트: 오늘의 할 일 웹 앱

## 결정 사항

- 결정: 백엔드에는 FastAPI를 사용하고, 데이터베이스는 SQLite를 사용한다.
- 결정: 데이터베이스 연결 정보는 .env 파일의 DATABASE_URL 환경변수로 관리한다.
- 결정: 프론트엔드는 단일 index.html 템플릿과 바닐라 JavaScript fetch를 사용해 페이지 전체를 새로고침하지 않고 동작하게 구현한다.
- 결정: 테스트는 pytest와 FastAPI TestClient를 사용해 API 동작을 검증한다.

## 근거

- FastAPI는 Python 기반 웹 API 구현에 적합하고, Pydantic과의 통합이 원활하다.
- SQLite는 이 범위의 단일 사용자 앱에 충분히 가볍고 간단하게 적용할 수 있다.
- Jinja2 템플릿과 바닐라 JavaScript를 조합하면 별도 빌드 도구 없이 빠르게 구현할 수 있다.
- pytest와 TestClient를 사용하면 API 레벨의 회귀 테스트를 쉽게 추가할 수 있다.

## 검토한 대안

- 대안 1: 브라우저 localStorage만 사용한다. 
  - 장점: 구현이 매우 단순하다.
  - 단점: 서버 재시작이나 다른 환경에서 상태를 공유하기 어렵다.
- 대안 2: PostgreSQL 등 서버형 데이터베이스를 사용한다.
  - 장점: 확장성과 운영성이 좋다.
  - 단점: 현재 범위와 복잡도에 비해 과도하다.
