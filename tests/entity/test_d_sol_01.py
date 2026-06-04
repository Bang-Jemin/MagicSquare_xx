from _approval import assert_matches_golden

from entity.sol import solve_blanks


def test_d_sol_01_step_a_success(grid_g1: list[list[int]]) -> None:
    # Given: G1 (빈칸 2개, Step A 유일 해)
    # When: solve_blanks(grid_g1)
    result = solve_blanks(grid_g1)
    # Then: int[6] Golden Master (1-index)
    assert_matches_golden(result, "d_sol_01_g1_step_a.approved.txt")
