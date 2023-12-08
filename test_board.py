from board import Board

# testing getting column and rows
board = Board()

def test_get_row_is_first_row():
    row = board.get_row(250)
    assert row == 0

def test_get_row_is_second_row():
    row = board.get_row(650)
    assert row == 1

def test_get_row_is_third_row():
    row = board.get_row(1050)
    assert row == 2

def test_get_col_is_first_col():
    col = board.get_column(250)
    assert col == 0

def test_get_col_is_second_col():
    col = board.get_column(650)
    assert col == 1

def test_get_col_is_third_col():
    col = board.get_column(1050)
    assert col == 2

def test_validate_sqr_can_be_clicked_ultimate_mode():
    uttt_board: Board = Board(ultimate_mode=True)
    top_left_sqr: Board = uttt_board.squares[0][0]
    top_left_sqr.active = True
    valid_sqr = uttt_board.validate_sqr(30, 30)
    assert valid_sqr == True

def test_validate_sqr_cannot_be_clicked_inactive_ultimate_mode():
    uttt_board: Board = Board(ultimate_mode=True)
    top_left_sqr: Board = uttt_board.squares[0][0]
    top_left_sqr.active = False
    valid_sqr = uttt_board.validate_sqr(30, 30)
    assert valid_sqr == False

def test_validate_sqr_cannot_be_clicked_already_clicked_ultimate_mode():
    uttt_board: Board = Board(ultimate_mode=True)
    top_left_sqr: Board = uttt_board.squares[0][0]
    top_left_sqr.squares[0][0] = 1
    valid_sqr = uttt_board.validate_sqr(30, 30)
    assert valid_sqr == False