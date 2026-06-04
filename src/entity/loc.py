"""빈칸 좌표 — FR-LOC-01."""

from entity.constants import BLANK_CELL, COORD_INDEX_BASE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """0(빈칸) 셀 좌표를 row-major, 1-index (row, col) 튜플 리스트로 반환."""
    coords: list[tuple[int, int]] = []
    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value == BLANK_CELL:
                coords.append(
                    (row_idx + COORD_INDEX_BASE, col_idx + COORD_INDEX_BASE)
                )
    return coords
