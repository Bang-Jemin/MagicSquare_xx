"""Golden Master approval — canonical text compare."""

from __future__ import annotations

import os
from pathlib import Path

GOLDEN_DIR = Path(__file__).resolve().parent / "golden"


def format_golden(actual: list[int] | str) -> str:
    """고정 포맷: 성공 int[6] 1-index · 실패 에러 코드 문자열."""
    if isinstance(actual, str):
        if not actual.startswith("E") or len(actual) != 4:
            raise TypeError(f"error code must be E00x string, got {actual!r}")
        return f"error: {actual}"
    if isinstance(actual, list) and len(actual) == 6 and all(isinstance(x, int) for x in actual):
        return "int6: " + ",".join(str(x) for x in actual)
    raise TypeError(f"unsupported golden value: {type(actual)!r}")


def assert_matches_golden(actual: list[int] | str, relative: str) -> None:
    """actual을 golden 파일과 비교. UPDATE_GOLDEN=1이면 기준 파일 갱신."""
    golden_path = GOLDEN_DIR / relative
    actual_text = format_golden(actual)
    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual_text + "\n", encoding="utf-8")
        return
    if not golden_path.is_file():
        raise AssertionError(f"golden missing: {golden_path}")
    expected_text = golden_path.read_text(encoding="utf-8").rstrip("\n")
    if actual_text != expected_text:
        raise AssertionError(
            f"golden mismatch ({relative}):\n"
            f"  expected: {expected_text!r}\n"
            f"  actual:   {actual_text!r}"
        )
    print(f"golden matched: {relative}")
