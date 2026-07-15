# 할 일 API 계약서

## 공통 규칙

- 모든 요청/응답 본문은 JSON으로 처리한다.
- 빈 제목은 422 Unprocessable Entity로 거절한다.
- 존재하지 않는 할 일 ID로 수정/삭제를 시도하면 404 Not Found를 반환한다.

## 엔드포인트

### GET /api/todos

- 설명: 할 일 목록을 조회한다.
- 쿼리 파라미터: status=all|active|completed
- 응답: Todo 배열

### POST /api/todos

- 설명: 새 할 일을 생성한다.
- 요청 본문: { "title": "할 일 제목" }
- 성공 응답: 생성된 Todo 객체
- 실패 응답: 422 (빈 제목)

### PATCH /api/todos/{id}

- 설명: 할 일 완료 상태를 변경한다.
- 요청 본문: { "completed": true }
- 성공 응답: 수정된 Todo 객체
- 실패 응답: 404 (없는 ID)

### DELETE /api/todos/{id}

- 설명: 할 일을 삭제한다.
- 성공 응답: 204 No Content
- 실패 응답: 404 (없는 ID)

### GET /

- 설명: 메인 HTML 화면을 반환한다.

### GET /health

- 설명: 서버 상태를 확인한다.
- 응답: { "status": "ok" }
