import argparse
import main as MazeSolver


def Main():
    pars = argparse.ArgumentParser()
    pars.add_argument("-o", "--outputfile", help="Output the result to a file", action="store_true")
    pars.add_argument("-i", "--inputfile", help="Output the result to a file", action="store_true")
    ars = pars.parse_args()
    if ars.outputfile:
        data = open("outputfile.txt", "a")
        if MazeSolver.res.solve_Maze(MazeSolver.maze) is False:
            data.write(str("-1"))
        else:
            for i in MazeSolver.res.solve_Maze(MazeSolver.maze):
                for result in i:
                    data.write(str(result) + " ")
                data.write('\n')


'''calling solve_Maze function from main file'''
MazeSolver.res.solve_Maze(MazeSolver.maze)

if __name__ == '__main__':
    Main()
