from edit_distance.utils import _init_matrix

def test_init_matrix_creates_matrix():
    # init
    rows = 3
    cols = 4
    
    # act
    matrix = _init_matrix(rows, cols)

    # assert
    assert len(matrix) == rows
    assert all(len(row) == cols for row in matrix)
