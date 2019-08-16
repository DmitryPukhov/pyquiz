class RobotInAGrid:
    """
    8.2
    Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
    The robot can only move in two directions, right and down, but certain cells are "off limits" such that
    the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
    the bottom right.
    """

    def __init__(self, stop_cells, r, c):
        """
        :param r:  rows in a grid
        :param c: cells in a grid
        """
        self.grid_r = r - 1
        self.grid_c = c - 1
        self.stop_cells = set(stop_cells)

    def find_path(self):
        """
        Algorithm to find a path for the robot from the top left to
        the bottom right.
        Algo: step right, if not possible, step left, if not possible go back
        """
        # Path is a list of cells
        path = [(0, 0)]
        # Visited cells, from which we went right or left
        went_right: set = set()
        went_down: set = set()

        r = 0
        c = 0
        while (r, c) != (self.grid_r, self.grid_c):
            # Step right if possible and we have not already been there
            if c < self.grid_c \
                    and (r, c) not in went_right \
                    and (r, c + 1) not in self.stop_cells:
                went_right.add((r, c))
                c += 1
                path.append((r, c))
            # Step down if possible and we have not already been there
            elif r < self.grid_r \
                    and (r, c) not in went_down \
                    and (r + 1, c) not in self.stop_cells:
                went_down.add((r, c))
                r += 1
                path.append((r, c))
            # No way to go right or down, go back
            else:
                (r, c) = path.pop()

        return path
