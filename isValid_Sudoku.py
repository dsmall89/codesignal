
'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column,
each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a 
valid Sudoku puzzle according to the layout rules described above. 
Note that the puzzle represented by grid does not have to be solvable.

'''
def sudoku2(grid):
    row, col, block = set(),set(),set()

    for row_idx in range(9):
        for col_idx in range(9):

            if(grid[row_idx][col_idx] != "."):
                #(Row|value) corrdinates
                r_key=  (row_idx,grid[row_idx][col_idx])
                #(Column|value) corrdinates
                c_key= (col_idx ,grid[row_idx][col_idx ])
                print("c-Key : "+ str(c_key))
                #(Row|Column|value) corrdinates
                b_key = (row_idx//3,col_idx//3, grid[row_idx][col_idx])
                # print("B-Key : "+ str(b_key))
                
                if ((r_key in row) or (c_key in col) or (b_key in block)): 
                    return False
                #Add value to set  
                row.add(r_key)
                col.add(c_key)
                block.add(b_key)
    return True


grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
print(sudoku2(grid))
