# TDD RED — 실패 테스트 먼저

MagicSquare_xx Dual-Track TDD **RED 단계만**. GREEN·REFACTOR·`src/` 구현 금지. 헌법: `.cursorrules`. 절차 SSOT: `.cursor/skills/magic-square-tdd/SKILL.md`, Test ID: `reference.md`.

## 필수 선언

**응답 첫 줄:**

```
Phase: red | Layer: entity | Track: Logic
```

- `Layer`: `entity` | `control` | `boundary`
- `Track`: `Logic` | `UI`
- Logic → `tests/entity/` 또는 `tests/control/`, `test_d_*`, ID `D-*`
- UI → `tests/boundary/`, `test_u_*`, ID `U-*`

## 절차

1. **ID 확인** — 이번 RED의 Test ID(`D-*` / `U-*`) 1개, PRD FR/C2C, 파일 경로 확정.
2. **Given 준비** — `tests/conftest.py`에 격자 픽스처만 (도메인 로직 없음).
3. **AAA 테스트 작성** — `tests/`만 수정.
   - **Arrange**: 4×4 격자 (빈칸 0×2). 10선 Logic이면 `\`·`/` 포함.
   - **Act**: 대상 함수 호출 (미구현 시 import → ImportError FAIL 허용).
   - **Assert**: PRD 기대값. 상수는 SSOT(`entity.constants`) import.
4. **pytest FAIL** — 아래 bash 실행. **FAIL 확인** = RED 완료.

## pytest 예시 (bash)

```bash
python -m pytest tests/entity/test_d_val_03.py::test_d_val_03_main_diagonal_sum_is_34 -v
python -m pytest tests/entity/test_d_val_05.py -v
python -m pytest -k "d_val_05" -v
```

RED 성공 조건: exit ≠ 0, 원인 = 미구현 / ImportError / `pytest.fail("RED: …")` / AssertionError.

## 보고

- **Test ID** (예: D-VAL-03)
- **FAIL 요약** (pytest 한 줄)
- **변경 파일** — `tests/`만

## 금지

- `src/` 수정
- Logic Track **Domain Mock** (`@patch` entity/control 핵심)
- **assert 완화**, `skip`, `xfail`, 통과용 더미 assert
