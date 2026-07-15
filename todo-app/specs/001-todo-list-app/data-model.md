# 데이터 모델: 오늘의 할 일 웹 앱

## 엔티티

### Todo

- id: 정수형 식별자
- title: 할 일 제목 문자열
- completed: 완료 여부 불리언
- created_at: 생성 시각
- updated_at: 마지막 수정 시각

## 관계

- 하나의 할 일 항목은 독립적으로 관리되며, 다른 엔티티와 관계를 가지지 않는다.

## 검증 규칙

- title은 공백이 아닌 문자열이어야 한다.
- completed 값은 불리언이어야 한다.
- 생성 시 created_at과 updated_at은 자동으로 설정된다.
