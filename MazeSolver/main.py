import fileinput


class Maze:
    '''Creating a matrix named sol with same size of maze and printing solution'''
    def solve_Maze(self, maze):
        sol = [[0 for i in range(matrix_Size_xaxis)]for j in range(matrix_Size_yaxis)]
        if res.solve_Maze_Util(maze, 0, 0, sol) is False:
            return False
        res.del_Wrong_Path(sol)
        return sol

    ''' This function solves the Maze problem using Backtracking.
    It returns false if no path is possible,otherwise return true and
    prints the path in the form of 1s.'''
    def solve_Maze_Util(self, maze, row_pointer, column_pointer, sol):
        # base case check if the pointers reached the end point
        if maze[matrix_Size_yaxis - 1][matrix_Size_xaxis - 1] == 1 and sol[matrix_Size_yaxis - 1][matrix_Size_xaxis - 1] == 1:
            return True

        # checks if it is safe to move to the pointers location by calling isSafe function
        if res.isSafe(maze, row_pointer, column_pointer, sol) is True:
            sol[row_pointer][column_pointer] = 1
            Maze.pointer_Mover(self, maze, row_pointer, column_pointer, sol)
        else:
            return False

        if sol[matrix_Size_yaxis - 1][matrix_Size_xaxis - 1] == 0:
            return False

    '''This function checks if it is safe to move to pointers location'''
    def isSafe(self, maze, row_pointer, column_pointer, sol):
        if row_pointer < matrix_Size_yaxis and column_pointer < matrix_Size_xaxis and maze[row_pointer][column_pointer] == 1:
            return True
        return False
        
    def pointer_Mover(self, maze, row_pointer, column_pointer, sol):
        # moving pointer rightward will be valid or not
        if res.solve_Maze_Util(maze, row_pointer, column_pointer + 1, sol) is True:
            return True
        # moving pointer leftward will be valid or not
        elif sol[row_pointer][column_pointer - 1] == 0 and maze[row_pointer][column_pointer - 1] == 1 and column_pointer != 0:
            res.solve_Maze_Util(maze, row_pointer, column_pointer - 1, sol)
            return True
        # moving pointer downward will be valid or not
        if res.solve_Maze_Util(maze, row_pointer + 1, column_pointer, sol) is True:
            return True
        # moving pointer upward will be valid or not
        elif sol[row_pointer - 1][column_pointer] == 0 and maze[row_pointer - 1][column_pointer] == 1 and row_pointer != 0:
            res.solve_Maze_Util(maze, row_pointer - 1, column_pointer, sol)
            return True
        return False

    '''Returns true if path was blocked'''
    def del_Wrong_Path(self, sol):
        for _ in range(0, matrix_Size_xaxis):
            for i in range(1, len(sol) - 1):
                for j in range(1, len(sol[0]) - 1):
                    if sol[i][j] == 1:
                        # checks every element in the sol Matrix with three directions blocked
                        if sol[i + 1][j] == 0 and sol[i - 1][j] == 0 and sol[i][j + 1] == 0:
                            sol[i][j] = 0
                        if sol[i + 1][j] == 0 and sol[i - 1][j] == 0 and sol[i][j - 1] == 0:
                            sol[i][j] = 0
                        if sol[i - 1][j] == 0 and sol[i][j + 1] == 0 and sol[i][j - 1] == 0:
                            sol[i][j] = 0
                        if sol[i + 1][j] == 0 and sol[i][j + 1] == 0 and sol[i][j - 1] == 0:
                            sol[i][j] = 0
        return True


''' Taking input from input.txt and Assigning it to maze'''
maze = []
Input = str(input("Enter the name of Input file:-"))
for line in fileinput.input(files=(Input)):
    element = list(map(int, line.split()))
    maze.append(element)

'''Maze Size'''
matrix_Size_xaxis = len(maze[0])
matrix_Size_yaxis = len(maze)

'''Assigning class to variable'''
res = Maze()
