# D-* Test ID (Logic Track)

| Test ID | PRD | Layer | 함수(예정) |
|---------|-----|-------|------------|
| D-VAL-01 | FR-VAL-01 | entity | `validate_rows()` |
| D-VAL-02 | FR-VAL-02 | entity | `validate_cols()` |
| D-VAL-03 | FR-VAL-03 | entity | `validate_main_diagonal()` |
| D-VAL-04 | FR-VAL-04 | entity | `validate_anti_diagonal()` |
| D-VAL-05 | FR-VAL-05 | entity | `validate_all_lines()` |
| D-LOC-01 | FR-LOC-01 | entity | `find_blank_coords()` |
| D-SOL-01 | FR-SOL-01 | entity | `solve_blanks()` |

파일명: `tests/entity/test_d_{val\|loc\|sol}_{nn}.py`
