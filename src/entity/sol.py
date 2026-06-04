"""빈칸 풀이 — FR-SOL-01."""

from itertools import permutations

from entity.constants import (
    BLANK_CELL,
    CELL_MAX,
    COORD_INDEX_BASE,
    GRID_SIZE,
    MAGIC_SUM,
)
from entity.loc import find_blank_coords


def solve_blanks(grid: list[list[int]]) -> list[int]:
    """빈칸 2개 대입 성공 시 int[6] [r1,c1,n1,r2,c2,n2] 1-index (row-major)."""
    coords = find_blank_coords(grid)
    missing = _missing_values(grid)
    solutions: list[list[int]] = []
    for nums in permutations(missing, len(coords)):
        if _all_lines_magic(_grid_with_fill(grid, coords, nums)):
            solutions.append(_to_int6(coords, nums))
    if len(solutions) != 1:
        raise ValueError("ambiguous or unsolvable blanks for Step A")
    return solutions[0]


def _missing_values(grid: list[list[int]]) -> list[int]:
    present = {
        value
        for row in grid
        for value in row
        if value != BLANK_CELL
    }
    return [
        value
        for value in range(COORD_INDEX_BASE, CELL_MAX + COORD_INDEX_BASE)
        if value not in present
    ]


def _grid_with_fill(
    grid: list[list[int]],
    coords: list[tuple[int, int]],
    nums: tuple[int, ...],
) -> list[list[int]]:
    filled = [row[:] for row in grid]
    for (row_1, col_1), num in zip(coords, nums, strict=True):
        filled[row_1 - COORD_INDEX_BASE][col_1 - COORD_INDEX_BASE] = num
    return filled


def _to_int6(coords: list[tuple[int, int]], nums: tuple[int, ...]) -> list[int]:
    return [
        coords[0][0],
        coords[0][1],
        nums[0],
        coords[1][0],
        coords[1][1],
        nums[1],
    ]


def _all_lines_magic(grid: list[list[int]]) -> bool:
    for row in grid:
        if sum(row) != MAGIC_SUM:
            return False
    for col in range(GRID_SIZE):
        if sum(grid[row][col] for row in range(GRID_SIZE)) != MAGIC_SUM:
            return False
    if sum(grid[i][i] for i in range(GRID_SIZE)) != MAGIC_SUM:
        return False
    if sum(grid[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)) != MAGIC_SUM:
        return False
    return True
