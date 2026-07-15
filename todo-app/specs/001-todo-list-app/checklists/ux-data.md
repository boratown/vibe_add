# 요구사항 품질 체크리스트: UX 및 데이터

**Purpose**: Validate whether the requirements are complete, clear, and testable for UX and persistence behaviors.
**Created**: 2026-07-15
**Feature**: [spec.md](../spec.md)

## UX 요구사항 품질

- [x] CHK001 빈 입력 처리 요구사항이 명확하게 정의되어 있는가? [Completeness, UX]
- [x] CHK002 삭제 전 확인 절차의 동작 방식이 명확하게 명시되어 있는가? [Clarity, UX]
- [x] CHK003 필터(전체/진행중/완료) 동작 기준이 요구사항에 명확히 포함되어 있는가? [Completeness, UX]
- [x] CHK004 남은 할 일 개수의 실시간 갱신 기준이 정의되어 있는가? [Clarity, UX]
- [x] CHK005 할 일이 없을 때 표시할 빈 상태 안내 문구의 요구사항이 구체적으로 적혀 있는가? [Completeness, UX]
- [x] CHK006 완료된 항목의 시각적 구분 기준(취소선, 흐린 색)이 요구사항에 명확히 포함되어 있는가? [Clarity, UX]
- [x] CHK007 완료/미완료 토글 동작이 사용자 관점에서 일관되게 설명되어 있는가? [Consistency, UX]

## 데이터 및 상태 유지 요구사항 품질

- [x] CHK008 서버 재시작 또는 페이지 새로고침 후에도 데이터가 유지된다는 요구사항이 명확한가? [Completeness, Data]
- [x] CHK009 데이터 유지 방식이 브라우저/서버 중 어느 쪽인지 명확히 정의되어 있는가? [Clarity, Data]
- [x] CHK010 잘못된 ID에 대한 요청 시 오류 처리 방식이 명시되어 있는가? [Completeness, Error Handling]
- [x] CHK011 삭제 또는 수정 대상이 없을 때 반환할 오류 상태가 요구사항에 포함되어 있는가? [Clarity, Error Handling]
- [x] CHK012 데이터 변경 후 화면에 반영되는 방식이 사용자 관점에서 명확하게 정의되어 있는가? [Consistency, Data]

## 회복/예외 흐름

- [x] CHK013 삭제 확인 절차를 취소했을 때 항목이 유지된다는 흐름이 요구사항에 포함되어 있는가? [Coverage, UX]
- [x] CHK014 빈 입력 시 새 항목이 추가되지 않고 안내 메시지가 보여진다는 흐름이 요구사항에 포함되어 있는가? [Coverage, UX]
- [x] CHK015 필터 조건에 해당하는 항목이 없을 때의 사용자 안내가 요구사항에 포함되어 있는가? [Coverage, UX]

## 측정 가능성

- [x] CHK016 요구사항이 구현자와 검토자 모두에게 동일하게 해석될 수 있는 수준으로 작성되었는가? [Measurability]
- [x] CHK017 UX 및 데이터 요구사항이 실제 테스트 시나리오로 변환 가능하도록 구체적인 기준을 포함하는가? [Measurability]
