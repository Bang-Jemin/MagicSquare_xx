# ECB · 계약 리뷰

MagicSquare_xx **코드 수정 금지**. `src/`, `tests/` 읽기만 하고 **ECB·계약 위반**을 표로 보고한다. 헌법: `.cursorrules`.

## 필수 선언

**응답 첫 줄:**

```
Phase: review | Scope: src/ tests/ | Track: Logic+UI
```

- 리뷰 대상: 사용자 지정 경로. 미지정 시 `src/`, `tests/` 전체.

## 절차

1. **범위 확인** — 리뷰할 파일·Layer 목록.
2. **5항목 점검** — 아래 체크리스트 기준으로 파일별 스캔.
3. **위반 표 작성** — 위반만 행 추가. 없으면 `위반 없음`.
4. **요약** — P0(계약 깨짐) / P1(권장) 개수.

## 체크리스트 (헌법)

| # | 항목 | 기준 |
|---|------|------|
| 1 | **import 방향** | `boundary → control → entity`. entity는 control/boundary import 금지. control은 boundary import 금지. boundary는 entity 직접 import 금지. |
| 2 | **entity E001~E005** | entity에서 E001~E005 문자열·코드·raise·return 없음. 입력 검증·에러 emit은 boundary/control. |
| 3 | **int[6] 1-index** | 성공 출력 `[r1,c1,n1,r2,c2,n2]`, 좌표 **1-index**(1~4). 0-index·길이≠6·계약 불일치는 boundary E005 후보. |
| 4 | **MagicConstant SSOT** | `34`, `16`, `4` 리터럴이 `entity.constants`(SSOT) 외 `src/`·`tests/`에 산재하지 않음. |
| 5 | **Logic Track Domain Mock** | `tests/entity/`, `tests/control/`, `test_d_*`에서 `@patch`·Mock으로 entity/control **핵심 도메인** 대체 없음. UI Track(`tests/boundary/`, `test_u_*`)은 Mock 허용. |

## 보고 (표)

**위반 있을 때:**

| 우선순위 | 체크 | 파일:줄 | 위반 내용 | 헌법 근거 |
|----------|------|---------|-----------|-----------|
| P0 | import 방향 | `src/entity/foo.py:3` | `from control import ...` | ECB |
| P0 | entity E001~E005 | `src/entity/bar.py:12` | entity에서 `E004` 반환 | 오류 경계 |
| P0 | int[6] 1-index | `src/boundary/out.py:8` | 좌표 0-index 반환 | 입출력 계약 |
| P1 | MagicConstant SSOT | `tests/entity/test_d_val_03.py:15` | `34` 리터럴 | SSOT |
| P0 | Logic Domain Mock | `tests/entity/test_d_loc_01.py:5` | `@patch` entity 핵심 | Dual-Track |

**위반 없을 때:**

| 결과 |
|------|
| ECB·계약 위반 없음 (점검 N파일) |

마지막에 **한 줄 요약** (P0 n건, P1 n건).

## 금지

- `src/`, `tests/`, 기타 파일 **수정·생성·삭제**
- pytest 실행으로 코드 변경, 자동 fix, refactor를 코드에 적용
- git commit (사용자 미요청 시)

## 선택 (코드 변경 없음)

정적 확인만:

```bash
grep -rn "E00[1-5]" src/entity/
grep -rn "from control\|from boundary" src/entity/
grep -rn "@patch\|Mock" tests/entity/ tests/control/
grep -rn "\b34\b\|\b16\b" src/ tests/ --include="*.py"
```

PowerShell: `Select-String -Path src\entity\*.py -Pattern "E00[1-5]"`
