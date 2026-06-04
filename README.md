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
│   └── PRD.md                       # 기능 요구사항 · C2C · Mom Test
├── Report/
│   └── 01.MagicSquare_ProblemDefinition_Report.md
├── Prompting/
│   └── 01.MagicSquare_ProblemDefinition_Report-Promt.md
├── src/                             # ⏳ 예정 (entity / control / boundary)
├── tests/                           # ⏳ 예정 (D-VAL-03~05 RED 우선)
└── .cursor/                         # ⏳ 예정 (rules · commands · skills · hooks)
```

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | PRD — FR·에러 코드·C2C·성공 기준 |
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

## C2C 추적 (우선순위)

| PRD | Test Case (RED) | Mom Test |
|-----|-----------------|----------|
| FR-VAL-03 | `validate_main_diagonal()` → 34 | 대각선 `\` 누락 재현 |
| FR-VAL-04 | `validate_anti_diagonal()` → 34 | 대각선 `/` 누락 재현 |
| FR-VAL-05 | `validate_all_lines()` → 10개 True | SC-1 |
| FR-LOC-01 | `find_blank_coords()` → 2좌표 | — |

## 현재 상태 · 다음 단계

| 항목 | 상태 |
|------|------|
| Mom Test · 문제 정의 (Report 01) | ✅ |
| PRD | ✅ |
| `.cursorrules` · Skill · Command · Hook | ⏳ |
| `pyproject.toml` · pytest harness | ⏳ |
| `src/` · `tests/` (D-VAL RED) | ⏳ |
| PyQt UI | ❌ (범위 외) |

**다음 작업**

1. `.cursorrules` — 4×4·10선=34·RED 우선 헌법
2. `/tdd-red` — **D-VAL-03**(`\`) RED + pytest FAIL
3. D-VAL-04~05 → SC-1~2 pytest로 증명

## 관련 프로젝트

[MagicSquare_1004](../docs/CursorAI-main/src/MagicSquare_1004/) — 동일 도메인 · TDD·ECB 구현 참고 (선행 세션)
