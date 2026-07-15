# 구현 계획서: 오늘의 할 일 웹 앱

**Branch**: `001-todo-list-app` | **Date**: 2026-07-15 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-todo-list-app/spec.md`

## Summary

이 기능은 Python과 FastAPI를 사용해 단일 사용자용 할 일 관리 웹 앱을 구현하는 것을 목표로 한다. 사용자는 할 일을 생성·완료·삭제하고 필터로 조회할 수 있으며, SQLite를 통해 데이터를 영속화한다. 메인 화면은 Jinja2 템플릿과 바닐라 JavaScript fetch로 구성되어 페이지 새로고침 없이 동작한다.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: FastAPI, SQLAlchemy 2.x, Jinja2, pytest, FastAPI TestClient

**Storage**: SQLite with DATABASE_URL from .env

**Testing**: pytest + FastAPI TestClient

**Target Platform**: Modern desktop and mobile browsers

**Project Type**: Web application

**Performance Goals**: Small-scale single-user app; responsive interaction for typical todo usage

**Constraints**: Must use SQLite and environment-based database configuration; must remain usable at 360px width

**Scale/Scope**: Single-user todo app with simple CRUD and filtering

## Constitution Check

- 환경 변수 기반 설정을 사용한다.
- 스펙에 명시된 범위 밖의 기능은 추가하지 않는다.
- 테스트를 먼저 검증한 뒤 구현을 진행한다.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-list-app/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── todos-api.md
└── tasks.md
```

### Source Code (repository root)

```text
app/
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── database.py
└── templates/
    └── index.html

tests/
└── test_api.py
```

**Structure Decision**: FastAPI 기반의 모듈형 구조를 사용한다. 라우팅은 app/main.py에서 담당하고, ORM 모델과 CRUD 로직은 각각 app/models.py, app/crud.py에 분리한다. 화면 템플릿은 app/templates/index.html에 두고, 바닐라 JavaScript가 API를 호출해 UI를 갱신한다.

## Complexity Tracking

No special complexity exceptions required.
