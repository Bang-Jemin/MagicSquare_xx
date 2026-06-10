"""격자 픽스처만 — 도메인 로직 없음."""

import pytest


@pytest.fixture
def grid_g0() -> list[list[int]]:
    """G0: 완전 마방진 (빈칸 0개)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1: 부분 마방진 — 0이 2개, (2,2)·(3,3) 1-index, row-major."""
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]
