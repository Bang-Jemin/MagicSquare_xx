# MagicSquare_xx

4×4 **부분 마방진**(빈칸 2개) 과제에서 **10선(행·열·대각선) 합=34** 판정을 빠짐없이 검증하기 위한 프로젝트입니다.

> **Mom Test에서 출발:** 행·열만 맞추고 대각선 검증을 빠뜨려 **약 20분**을 추가로 쓴 경험을, **기계적·재현 가능한 판정**으로 바꾸는 것이 목표입니다.

## 진짜 문제 (한 문장)

지난주 OO 과제에서 빈칸 2개를 채운 뒤 행·열 합은 맞췄지만 **10선 중 대각선 하나**를 검증에서 빠뜨려, 틀린 상태를 끝까지 못 잡고 약 20분을 추가로 썼다.

### Mom Test 증거

1. 「지난주 OO 과제에서」
2. 「빈칸 2개 넣고 행·열·대각선 합 맞췄는데」
3. 「대각선 하나를 빼먹어서 20분 날렸다.」

**표면 문제 (하지 않을 정의):** 「4×4 마방진 검증/풀이 프로그램」·「PyQt 완성 앱」을 만든다.

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (중복 없음) |
| 빈칸 | **정확히 2개** (`0`) |
| 마법 상수 | **34** |
| 검증 대상 | **10선** — 행 4 + 열 4 + `\` + `/` |

## 성공 기준 (Mom Test)

| ID | 기준 | Mom Test 연결 |
|----|------|---------------|
| SC-1 | **10선 합 전부** 계산·검증 (행·열만 X) | 「대각선 합 맞췄는데」→ `\`·`/` **둘 다** |
| SC-2 | 한 줄이라도 ≠34 → **실패 + 깨진 줄 식별** | 「대각선 하나 빼먹어서」 |
| SC-3 | 동일 유형에서 원인 특정 **1분 이내** | 「20분 날렸다」 |

## 세션 3 주제

10선 판정을 빠뜨려 ~20분을 낭비하는 문제를, **"빠진 줄(특히 대각선)이 바로 드러나게"** Cursor Rule·Command·Test Loop까지 고정한다.

| 계층 | 예정 산출 |
|------|-----------|
| **Rule** | `.cursorrules` — 10선=34, RED 우선, ECB·Dual-Track |
| **Command** | `/tdd-red`, `/pytest-logic` 또는 `/review-ecb` |
| **(Skill)** | `magic-square-tdd` — 10선 체크리스트, C2C |
| **Test Loop** | `tests/entity/test_d_val_*.py` — D-VAL-03~05 RED |

## 아키텍처 (예정)

- **ECB:** `boundary → control → entity`
- **Dual-Track TDD:** Logic Track (`D-*`) + UI Track (`U-*`)
- **RED 우선:** pytest FAIL 확인 → GREEN → REFACTOR

## 프로젝트 구조

```
MagicSquare_xx/
├── README.md
├── docs/
│   ├── PRD.md
│   └── TDD-RED-TODO.md              # RED 체크리스트 SSOT
├── Report/
│   └── 01.MagicSquare_ProblemDefinition_Report.md
├── Prompting/
│   └── 01.MagicSquare_ProblemDefinition_Report-Promt.md
├── src/                             # ⏳ GREEN부터 (entity / control / boundary)
├── tests/                           # ⏳ RED — conftest · test_d_* · test_u_*
└── .cursor/                         # rules · commands · skills
```

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | PRD — FR·에러 코드·C2C·성공 기준 |
| [docs/TDD-RED-TODO.md](docs/TDD-RED-TODO.md) | TDD RED 체크리스트 (Boundary `U-*` · Logic `D-*`) |
| [Report/01](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test · R-G-I-O · 세션 3 · 범위 |
| [Prompting/01](Prompting/01.MagicSquare_ProblemDefinition_Report-Promt.md) | STEP 1 Mom Test 인터뷰 Transcript |

## 범위

**In**
- 4×4, 빈칸 2개, 10선=34 판정
- 빈칸 좌표 탐색, 후보 값 검증
- Mom Test 문제 정의 · PRD · Cursor Rule/Command/Test Loop

**Out**
- PyQt 완성 앱 · 배포 (1차 목표 아님)
- 3×3 / 5×5 · 마방진 자동 생성
- ECB 분류·슬라이드 설계만으로 "문제 해결" 처리
- "대충 맞는 것 같다" 수동 확인만으로 완료 처리

## TDD RED 체크리스트

> 상세 설계·표: [docs/TDD-RED-TODO.md](docs/TDD-RED-TODO.md) · RED는 **`tests/`만** 수정 · 각 항목마다 **`pytest` FAIL** 확인

### 진행 요약

| 항목 | 상태 |
|------|------|
| Harness (`pyproject.toml`, `tests/` 골격) | ✅ |
| `tests/conftest.py` 픽스처 G0/G1 | ✅ |
| Logic RED (`D-*`) | ⏳ (D-LOC-01 RED 완료) |
| Boundary RED (`U-*`) | ⬜ |

### 공통 — RED 게이트

- [ ] **RED-00** `Phase: red` 선언 후 `tests/`만 수정 (`src/` 금지)
- [ ] **RED-01** `pytest` exit ≠ 0 확인 (`ImportError` / `AssertionError` / `pytest.fail("RED: …")` 허용)
- [ ] **RED-02** Logic Track Domain Mock 금지 · UI Track Mock 허용
- [ ] **RED-03** `pytest.skip` · `xfail` · assert 완화·통과용 더미 assert 금지

### 선행 — Given 픽스처 (`tests/conftest.py`)

| ID | 설명 |
|----|------|
| **G0** | 완전 마방진 `[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]` |
| **G1** | 부분 마방진 `[[16,3,2,13],[5,0,11,8],[9,6,0,12],[4,15,14,1]]` — 빈칸 (2,2)·(3,3) 1-index |

- [x] **FIX-01** `grid_g0` 픽스처 (G0)
- [x] **FIX-02** `grid_g1` 픽스처 (G1) — 미존재 수 `[7, 10]`
- [ ] **FIX-03** 마방진 상수 `34` — `entity.constants` SSOT import (리터럴 산재 금지)

### Logic Track — `tests/entity/test_d_*.py` *(권장 순서)*

- [ ] **D-VAL-03** `validate_main_diagonal()` — G0 → `\` 합 = 34 · Mom Test **최우선**
- [ ] **D-VAL-04** `validate_anti_diagonal()` — G0 → `/` 합 = 34
- [ ] **D-VAL-05** `validate_all_lines()` — G0 → 10선 전부 34 (SC-1)
- [ ] **D-VAL-01** `validate_rows()` — G0 → 행 4개 합 = 34
- [ ] **D-VAL-02** `validate_cols()` — G0 → 열 4개 합 = 34
- [x] **D-LOC-01** `find_blank_coords()` — G1 → `[(2,2),(3,3)]` *(RED 스켈레톤·pytest FAIL 확인)*
- [ ] **D-SOL-01** `solve_blanks()` — G1 Step A 성공
- [ ] **D-MIS-01** `find_not_exist_nums()` — G1 → `[7, 10]` 오름차순

### Boundary / UI Track — `tests/boundary/test_u_*.py` *(우선: U-IN-01 → U-IN-02)*

**입력 (U-IN)**

- [ ] **U-IN-01** `grid=None` → `E003`
- [ ] **U-IN-02** `grid=3×4` → `E001`
- [ ] **U-IN-03** 빈칸 0개 → `E002`
- [ ] **U-IN-04** 값 1~16 밖 → `E003`
- [ ] **U-IN-05** 1~16 중복 → `E003`

**출력·흐름 (U-OUT, U-FLOW)**

- [ ] **U-OUT-01** 유효 G1 → `len(result)==6`, `[r1,c1,n1,r2,c2,n2]` 1-index
- [ ] **U-OUT-02** 10선 중 1줄 ≠34 → `E004` + 깨진 줄 식별 (SC-2)
- [ ] **U-FLOW-01** 유효 G1 → boundary → control → entity 호출 순
- [ ] **U-FLOW-02** `grid=None` → `execute()` 0회 (조기 종료)

### RED 확인용 pytest

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
python -m pytest tests/entity/test_d_val_03.py -v
python -m pytest tests/boundary/test_u_in_01.py -v
python -m pytest tests/entity/ tests/boundary/ -v
```

## 현재 상태

| 항목 | 상태 |
|------|------|
| Mom Test · 문제 정의 (Report 01) | ✅ |
| PRD · [TDD-RED-TODO](docs/TDD-RED-TODO.md) | ✅ |
| `.cursorrules` · Skill · `/tdd-red` | ✅ |
| `pyproject.toml` · pytest harness | ✅ |
| RED 테스트 (`tests/` · 위 체크리스트) | ⏳ (D-LOC-01 완료) |
| `src/` GREEN 구현 | ⬜ |
| PyQt UI | ❌ (범위 외) |

## 관련 프로젝트

[MagicSquare_xx](../docs/CursorAI-main/src/MagicSquare_xx/) — 동일 도메인 · TDD·ECB 구현 참고 (선행 세션)
