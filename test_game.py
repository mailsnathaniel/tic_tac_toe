import pytest

@pytest.fixture
def supply_board_bestpossiblemove():
    board = [['1', '2', '-'],
             ['2', '1', '-'],
             ['-', '-', '-']]
    return board

@pytest.fixture
def supply_board_validate():
    board = [['1', '1', '1'],
             ['1', '1', '2'],
             ['1', '1', '1']]
    return board, 3

@pytest.fixture
def supply_board_bestpossiblemove2():
    board = [['4', '-', '8'],
             ['-', '5', '-'],
             ['-', '-', '-']]
    return board


# Test Case for a row win
def test_row_win(supply_board_validate):
    import validate
    obj = validate.Validate()
    board, win_num = supply_board_validate
    res = obj.row_win(board, win_num)
    assert res==True, "Row Win Case Failed"

# Test Case for a Column win
def test_col_win(supply_board_validate):
    import validate
    obj = validate.Validate()
    board, win_num = supply_board_validate
    res = obj.col_win(board, win_num)
    assert res==True, "Column Win Case Failed"

# Test Case for a Diag win
def test_diagonal_win(supply_board_validate):
    import validate
    obj = validate.Validate()
    board, win_num = supply_board_validate
    res = obj.diag_win(board, win_num)
    assert res==True, "Diagonal Win Case Failed"

# Test Case for a Best Possible Move
def test_bestposiblemove_pattern(supply_board_bestpossiblemove):
   import metainfo
   metaObj = metainfo.metainfo(3)
   import minimax
   obj = minimax.minimax(metaObj)
   board = supply_board_bestpossiblemove
   pos = obj.findBestMove(board, '2', '1')
   assert pos==(2,2), "Computer's Best Possible Move Test Case Failed"

# Test Case for a Best Possible Move - Number Pattern
def test_bestposiblemove_number(supply_board_bestpossiblemove2):
   import metainfo
   metaObj = metainfo.metainfo(4)
   import minimax
   obj = minimax.minimax(metaObj)
   board = supply_board_bestpossiblemove2
   pos = obj.findBestMove(board, '2', '1')
   assert pos==(2,0), "Computer's Best Possible Move Test Case Failed"
