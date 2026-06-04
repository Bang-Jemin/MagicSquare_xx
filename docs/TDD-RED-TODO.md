# TDD RED To-Do — MagicSquare_xx

> SSOT: [PRD.md](PRD.md) · [.cursorrules](../.cursorrules) · [magic-square-tdd/reference.md](../.cursor/skills/magic-square-tdd/reference.md)  
> Dual-Track RED 설계표를 **실행 가능한 체크리스트**로 정리한다. GREEN·`src/` 구현은 본 문서 범위 밖.

## 상태

| 항목 | 상태 |
|------|------|
| Harness (`pyproject.toml`, `tests/` 골격) | ✅ |
| `tests/conftest.py` 픽스처 G0/G1 | ✅ |
| Boundary RED (`U-*`) | ⬜ |
| Logic RED (`D-*`) | ⏳ (D-LOC-01 RED 완료) |

---

## 공통 — RED 게이트

- [ ] **RED-00** `Phase: red` 선언 후 `tests/`만 수정 (`src/` 금지)
- [ ] **RED-01** `pytest` exit ≠ 0 확인 (`ImportError` / `AssertionError` / `pytest.fail("RED: …")` 허용)
- [ ] **RED-02** Logic Track Domain Mock 금지 · UI Track Mock 허용
- [ ] **RED-03** `pytest.skip` · `xfail` · assert 완화·통과용 더미 assert 금지

---

## 선행 — Given 픽스처 (`tests/conftest.py`)

도메인 로직 없이 격자 데이터만 정의한다.

| ID | 설명 | 4×4 격자 (0=빈칸) |
|----|------|-------------------|
| **G0** | 완전 마방진 | `[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]` |
| **G1** | 부분 마방진 (빈칸 2개) | `[[16,3,2,13],[5,0,11,8],[9,6,0,12],[4,15,14,1]]` |

- [x] **FIX-01** `grid_g0` 픽스처 — 완전 마방진 (G0)
- [x] **FIX-02** `grid_g1` 픽스처 — 빈칸 (2,2)·(3,3) **1-index**, 미존재 수 `[7, 10]` (G1)
- [ ] **FIX-03** 마방진 상수 `34`는 `entity.constants` SSOT import (리터럴 산재 금지)

---

## Boundary / UI Track — `tests/boundary/test_u_*.py`

**Layer:** `boundary` · **Track:** UI · 에러 코드 **E001~E007**는 boundary 최종 반환

### 입력 검증 (U-IN)

| Test ID | Given | Then | Expected RED Failure |
|---------|-------|------|----------------------|
| U-IN-01 | `grid=None` | `E003` `INVALID_NULL` | `ModuleNotFoundError` / `ImportError` |
| U-IN-02 | `grid=3×4` | `E001` `INVALID_SIZE` | `AssertionError` |
| U-IN-03 | 빈칸 0개 | `E002` `INVALID_BLANKS` | `AssertionError` |
| U-IN-04 | 값 1~16 밖 (FR-IN-03) | `E003` | `AssertionError` |
| U-IN-05 | 1~16 중복 (FR-IN-05) | `E003` | `AssertionError` |

- [ ] **U-IN-01** — `tests/boundary/test_u_in_01.py` 작성 → `pytest` FAIL 확인
- [ ] **U-IN-02** — `tests/boundary/test_u_in_02.py` 작성 → `pytest` FAIL 확인
- [ ] **U-IN-03** — `tests/boundary/test_u_in_03.py` 작성 → `pytest` FAIL 확인
- [ ] **U-IN-04** — `tests/boundary/test_u_in_04.py` 작성 → `pytest` FAIL 확인
- [ ] **U-IN-05** — `tests/boundary/test_u_in_05.py` 작성 → `pytest` FAIL 확인

### 출력·흐름 (U-OUT, U-FLOW)

| Test ID | Given | Then | Expected RED Failure |
|---------|-------|------|----------------------|
| U-OUT-01 | 유효 **G1** | `len(result)==6`, `[r1,c1,n1,r2,c2,n2]` 1-index | `pytest.fail()` RED |
| U-OUT-02 | 10선 중 1줄 ≠34 | `E004` + 깨진 줄 식별 (SC-2) | `pytest.fail()` RED |
| U-FLOW-01 | 유효 **G1** | boundary → control → entity 호출 순 | `pytest.fail()` RED |
| U-FLOW-02 | `grid=None` | `execute()` **0회** (조기 종료) | `pytest.fail()` RED |

- [ ] **U-OUT-01** — `tests/boundary/test_u_out_01.py` 작성 → `pytest` FAIL 확인
- [ ] **U-OUT-02** — `tests/boundary/test_u_out_02.py` 작성 → `pytest` FAIL 확인
- [ ] **U-FLOW-01** — `tests/boundary/test_u_flow_01.py` 작성 → `pytest` FAIL 확인
- [ ] **U-FLOW-02** — `tests/boundary/test_u_flow_02.py` 작성 → `pytest` FAIL 확인

**UI Track 우선순위:** U-IN-01 → U-IN-02 → (이후 U-IN-03~05, U-OUT, U-FLOW)

---

## Logic / Domain Track — `tests/entity/test_d_*.py`

**Layer:** `entity` · **Track:** Logic · entity는 **E001~E005 emit 금지**

### 요약 설계 (워크북·슬라이드 ID)

| Test ID | 대상 함수 | Given → Then | Invariant |
|---------|-----------|--------------|-----------|
| D-LOC-01 | `find_blank_coords()` | **G1** → `[(2,2),(3,3)]` | I6 row-major, 1-index |
| D-MIS-01 | `find_not_exist_nums()` | **G1** → `[7, 10]` 오름차순 | I7, I11 |
| D-VAL-01† | `is_magic_square()` (통합) | **G0** → `True` | I1~I5 |
| D-SOL-01 | `solve_blanks()` | **G1** Step A 성공 | I8 |

† PRD SSOT에서는 10선을 아래 **D-VAL-01~05**로 분리한다.

- [x] **D-LOC-01** — `tests/entity/test_d_loc_01.py` → FAIL (`pytest.fail` RED 확인)
- [ ] **D-MIS-01** — `tests/entity/test_d_mis_01.py` → FAIL (`ImportError` / `AssertionError`)
- [ ] **D-SOL-01** — `tests/entity/test_d_sol_01.py` → FAIL (`pytest.fail()` RED)

### 공식 10선 검증 (PRD · Mom Test SSOT)

| Test ID | PRD | 대상 함수 | Given → Then | Expected RED Failure |
|---------|-----|-----------|--------------|----------------------|
| D-VAL-01 | FR-VAL-01 | `validate_rows()` | **G0** → 행 4개 합 = 34 | `AssertionError` |
| D-VAL-02 | FR-VAL-02 | `validate_cols()` | **G0** → 열 4개 합 = 34 | `AssertionError` |
| D-VAL-03 | FR-VAL-03 | `validate_main_diagonal()` | **G0** → `\` 합 = 34 | `AssertionError` |
| D-VAL-04 | FR-VAL-04 | `validate_anti_diagonal()` | **G0** → `/` 합 = 34 | `AssertionError` |
| D-VAL-05 | FR-VAL-05 | `validate_all_lines()` | **G0** → 10선 전부 34 | `pytest.fail()` RED |

- [ ] **D-VAL-01** — `tests/entity/test_d_val_01.py` → FAIL
- [ ] **D-VAL-02** — `tests/entity/test_d_val_02.py` → FAIL
- [ ] **D-VAL-03** — `tests/entity/test_d_val_03.py` → FAIL *(Mom Test `\` — **최우선**)*
- [ ] **D-VAL-04** — `tests/entity/test_d_val_04.py` → FAIL *(Mom Test `/`)*
- [ ] **D-VAL-05** — `tests/entity/test_d_val_05.py` → FAIL *(SC-1: 10선 전체)*

**Logic Track 권장 순서:** D-VAL-03 → D-VAL-04 → D-VAL-05 → D-LOC-01 → D-SOL-01 → D-MIS-01

---

## Invariant 참고 (I*)

| ID | 의미 |
|----|------|
| I1~I4 | 행·열·`\`·`/` 각 합 = **34** |
| I5 | 1~16 중복 없음 (완전 격자) |
| I6 | 빈칸 좌표 **row-major**, **1-index** |
| I7 / I11 | 미사용 수 **오름차순** |
| I8 | 빈칸 2개 대입 후 10선=34 (풀이 Step A) |

---

## C2C 추적

```
PRD FR-*  →  Test ID (D-* / U-*)  →  tests/{layer}/test_{d|u}_*.py  →  pytest FAIL (RED)  →  GREEN
```

| PRD | Test ID | Mom Test |
|-----|---------|----------|
| FR-VAL-03 | D-VAL-03 | 대각선 `\` 누락 재현 |
| FR-VAL-04 | D-VAL-04 | 대각선 `/` 누락 재현 |
| FR-VAL-05 | D-VAL-05 | SC-1 (10선 전부) |
| FR-LOC-01 | D-LOC-01 | 빈칸 2좌표 |
| FR-IN-01~05 | U-IN-01~05 | 입력 거부 |
| FR-OUT-01~02 | U-OUT-01~02 | 출력 계약 |

---

## pytest 명령 (RED 확인용)

```bash
python -m pytest tests/entity/test_d_val_03.py -v
python -m pytest tests/boundary/test_u_in_01.py -v
python -m pytest tests/entity/ tests/boundary/ -v
```

---

## 다음 Phase (본 To-Do 완료 후)

- [ ] **GREEN** — 대상 Test ID 1개씩 `src/` 최소 구현 → PASS
- [ ] **REFACTOR** — 전체 `pytest` PASS 유지하며 구조 정리
