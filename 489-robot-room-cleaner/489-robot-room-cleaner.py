# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

from typing import Set, Tuple


class Solution:
    def cleanRoom(self, robot):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited: Set[Tuple[int, int]] = set()

        def goBack():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(coord: Tuple[int, int], d: int):
            visited.add(coord)
            robot.clean()
            for i in range(4):
                newD = (d + i) % 4
                newX, newY = coord[0] + \
                    directions[newD][0], coord[1] + directions[newD][1]
                if (newX, newY) not in visited and robot.move():
                    backtrack((newX, newY), newD)
                    # goBack() Note that I can goBack here. This is controlling children returning call in parent func
                    # bit of a inversion of control?
                robot.turnLeft()
            goBack()  # Note that I instead chose to goBack here. I think this is more intuitive
        backtrack((0, 0), 0)
