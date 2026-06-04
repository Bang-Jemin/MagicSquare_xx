# Golden Master — Logic Track (GREEN PASS SSOT)

> **Golden Master** = RED에서 고정한 Given·When·Then이 **pytest PASS**로 증명된 기준선.  
> REFACTOR·후속 Test ID는 이 출력을 깨지 않아야 한다.

## 진행 요약

| Test ID | PRD | Layer | GREEN PASS | Golden Master (Then) |
|---------|-----|-------|------------|----------------------|
| **D-LOC-01** | FR-LOC-01 | entity | ✅ | `[(2, 2), (3, 3)]` — G1, 1-index, row-major |
| **D-SOL-01** | FR-SOL-01 | entity | ✅ | `int6: 2,2,10,3,3,7` — approval golden |

---

## Approval Golden (`tests/_approval.py`)

| 항목 | 값 |
|------|-----|
| **헬퍼** | `assert_matches_golden(actual, relative)` |
| **포맷 (성공)** | `int6: r1,c1,n1,r2,c2,n2` (1-index) |
| **포맷 (실패)** | `error: E00x` |
| **기준 갱신** | `UPDATE_GOLDEN=1 python -m pytest …` |
| **수동 편집** | 금지 — 갱신은 pytest로만 |

### D-SOL-01 — `solve_blanks` Step A (G1)

| 항목 | 값 |
|------|-----|
| **Golden 파일** | `tests/golden/d_sol_01_g1_step_a.approved.txt` |
| **Given** | `grid_g1` |
| **When** | `solve_blanks(grid_g1)` |
| **Then** | `int6: 2,2,10,3,3,7` |

```bash
# 기준 생성 (PowerShell)
$env:UPDATE_GOLDEN="1"; python -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v

# 검증 (matched)
python -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v -s
```

---

## D-LOC-01 — `find_blank_coords`

| 항목 | 값 |
|------|-----|
| **Given** | `grid_g1` — `tests/conftest.py` |
| **When** | `find_blank_coords(grid)` — `src/entity/loc.py` |
| **Then (Golden Master)** | `[(2, 2), (3, 3)]` |
| **Invariant** | I6 row-major, 1-index |
| **SSOT 상수** | `entity.constants` — `BLANK_CELL`, `COORD_INDEX_BASE` |

### PASS 확인 (가상환경 권장)

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
python -m pytest tests/entity/test_d_loc_01.py -v
```

### Harness 주의

- `tests/entity/__init__.py` **없음** — `tests.entity`가 `src/entity` import를 가리지 않도록 함.
- `pyproject.toml` → `pythonpath = ["src"]`

### ECB (D-LOC-01 GREEN)

| 점검 | 결과 |
|------|------|
| entity → control/boundary import | 없음 |
| E001~E005 in `src/entity/` | 없음 |
| Logic Track Domain Mock | 없음 |

---

## 다음 Golden Master 후보

| 순서 | Test ID | 비고 |
|------|---------|------|
| 1 | D-SOL-01 | ✅ approval golden |
| 2 | D-VAL-03 | Mom Test `\` — RED 후 GREEN |
| 2 | D-VAL-04 | `/` |
| 3 | D-VAL-05 | SC-1 10선 |
