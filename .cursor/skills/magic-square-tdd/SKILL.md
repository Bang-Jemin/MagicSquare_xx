---
name: magic-square-tdd
description: MagicSquare_xx Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. Use when writing or running pytest for MagicSquare_xx, RED/GREEN/REFACTOR, Logic or UI Track, D-* or U-* tests, entity/control/boundary layers, 10-line validation, or ECB/Mock/error-code rules.
---

# magic-square-tdd

MagicSquare_xx **Dual-Track TDD + ECB** 절차 매뉴얼. 헌법 SSOT: `.cursorrules` → `docs/PRD.md` → `Report/*`.

Test ID 목록: [reference.md](reference.md)

---

## 언제 이 Skill을 켜는가

| 트리거 | 예 |
|--------|-----|
| TDD 사이클 | RED / GREEN / REFACTOR, `/tdd-red` 등 TDD 요청 |
| 테스트 작성·실행 | `test_d_*`, `test_u_*`, D-VAL, D-LOC, U-IN |
| Layer 작업 | `src/entity`, `src/control`, `src/boundary` 구현·리뷰 |
| Mom Test 재현 | 10선=34, `\`·`/` 대각선, SC-1~2 검증 |
| ECB·계약 점검 | import 방향, Mock 허용/금지, E001~E007 |

**끄거나 생략:** README·Report 문서만 편집, git commit(사용자 미요청), 3×3/5×5/PyQt 완성 앱.

---

## Logic Track vs UI Track

| | **Logic Track** | **UI Track** |
|---|-----------------|--------------|
| Layer | `entity`, `control` | `boundary` |
| Test ID | `D-*` | `U-*` |
| 파일 | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` | `tests/boundary/test_u_*.py` |
| Mock | **Domain Mock 금지** (`@patch` entity/control 대체 불가) | Mock **허용** (I/O·UI stub) |
| RED 수정 범위 | `tests/`만 | `tests/`만 |
| GREEN 수정 범위 | 해당 Layer `src/` | `src/boundary/` (+ 필요 시 `src/control/`) |
| 우선순위 | D-VAL-03~05 (Mom Test 대각선) | U-IN-01~02 (입력 거부) |

---

## ECB · Mock · E001~E007

### import (ECB)

```
boundary → control → entity
```

| 허용 | 금지 |
|------|------|
| boundary → control, entity | entity → control, boundary |
| control → entity | control → boundary |
| entity → entity (동일 layer) | boundary → entity (control 생략) |

### Mock

| Track | Mock | 이유 |
|-------|------|------|
| Logic | **금지** | 도메인(10선·풀이)을 Mock으로 우회하면 Mom Test 재현 불가 |
| UI | **허용** | boundary I/O·PyQt stub으로 입력/출력 계약만 검증 |

### 오류 코드

| 코드 | 담당 | entity |
|------|------|--------|
| E001~E005 | boundary (최종 반환) | **raise·return·emit 금지** — 로직만 |
| E006~E007 | entity 결과 → control/boundary 매핑 | 판정 결과만 반환 |

- entity: 10선 합 **계산·불일치 판정** OK — **E004 문자열/코드 부여는 boundary**

---

## RED (5~7단계)

**선언:** `Phase: red | Layer: … | Track: Logic|UI`

1. **Test ID 확정** — PRD FR ↔ `D-*`/`U-*` ↔ 파일 경로 ([reference.md](reference.md))
2. **Given 준비** — `tests/conftest.py`에 격자 픽스처만 (도메인 로직 없음)
3. **AAA 테스트 작성** — `tests/`만 수정; Given/When/Then 주석
4. **Then** — 기대값 명시 + `pytest.fail("RED: {TestID} — …")` 또는 미구현 호출로 **의도적 FAIL**
5. **금지 확인** — `src/` 미수정, skip/xfail/통과 더미 assert 없음, Logic Track Mock 없음
6. **pytest 실행** — `python -m pytest tests/{layer}/test_{d|u}_*.py -v` → **FAIL 확인**
7. **완료 보고** (아래 표)

---

## GREEN (5~7단계)

**선언:** `Phase: green | Layer: … | Track: Logic|UI`

1. **대상 RED 확인** — 어떤 Test ID를 PASS로 만들지 1개(또는 묶음) 명시
2. **최소 구현** — 해당 Layer `src/`만; boundary→control→entity 순 준수
3. **MagicConstant SSOT** — `34`/`16`/`4`는 `entity.constants` import; 리터럴 산재 금지
4. **entity E001~E005** — entity에 에러 코드 문자열·raise·return 없음
5. **pytest 실행** — 대상 테스트 **PASS** + 기존 테스트 회귀 없음
6. **10선 체크** (D-VAL 관련) — R1~R4, C1~C4, `\`, `/` **전부** 검증 경로 포함 (Mom Test SC-1)
7. **완료 보고**

---

## REFACTOR (5~7단계)

**선언:** `Phase: refactor | Layer: … | Track: Logic|UI`

1. **전제** — REFACTOR 대상 테스트 **이미 GREEN**
2. **범위** — 동작 변경·기능 추가·버그 수정 **금지**; 구조·이름·중복만
3. **ECB·SSOT 유지** — import 방향, entity E001~E005, MagicConstant 위반 없음
4. **pytest (전)** — `python -m pytest` 전체 PASS 스냅샷
5. **리팩터** — smell 제거(중복 상수, 긴 함수 분리 등) 최소 diff
6. **pytest (후)** — 전체 PASS; assert 완화·skip·xfail **금지**
7. **완료 보고**

---

## Test / Review Loop — pytest 언제·무엇을

| 시점 | 명령 | 기대 |
|------|------|------|
| Harness 확인 | `python -m pytest --collect-only` | 테스트 0개(exit 5) 또는 수집 목록 |
| RED 직후 | `python -m pytest tests/entity/test_d_val_03.py -v` (해당 파일) | **FAIL** (Mom Test `\` 재현) |
| GREEN 직후 | 동일 파일 + `python -m pytest tests/ -v` | 대상 **PASS**, 회귀 없음 |
| REFACTOR 전·후 | `python -m pytest tests/ -v` | 전부 **PASS** |
| Logic Track 묶음 | `python -m pytest tests/entity/ tests/control/ -v` | D-* 전체 |
| UI Track | `python -m pytest tests/boundary/ -v` | U-* |
| ECB Review (코드 변경 없음) | `grep` E001~E005 in `src/entity/`, import 방향 | 위반 0건 |

**Mom Test 우선 RED 순서:** D-VAL-03 (`\`) → D-VAL-04 (`/`) → D-VAL-05 (10선) → D-LOC-01 → D-SOL-01

---

## 완료 보고 항목

매 Phase 종료 시 아래를 **한국어**로 보고:

| # | 항목 |
|---|------|
| 1 | **Phase / Layer / Track** 선언 |
| 2 | **Test ID** (예: D-VAL-03) |
| 3 | **PRD FR** 연결 (예: FR-VAL-03) |
| 4 | **변경 파일** 목록 |
| 5 | **pytest 결과** — FAIL 또는 PASS 요약 (exit code, 실패 메시지 1줄) |
| 6 | **ECB·Mock·E001~E005** 준수 여부 (해당 시) |
| 7 | **다음 Phase** 제안 (RED→GREEN→REFACTOR) |

---

## 금지 (전 Phase 공통)

- `pytest.skip`, `pytest.mark.xfail`, assert 완화·삭제
- Logic Track Domain Mock
- entity에서 E001~E005 emit
- RED 중 `src/` 수정 (스켈레톤 stub도 GREEN까지 보류)
- git commit / push (사용자 명시 요청 전)
- 3×3·5×5, PyQt 완성 앱, 마방진 자동 생성
