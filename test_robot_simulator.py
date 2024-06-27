import unittest
from robot_simulator import ToyRobotSimulator, execute_commands

class TestToyRobotSimulator(unittest.TestCase):
    def test_place_and_report(self):
        robot = execute_commands(['PLACE 0,0,NORTH', 'REPORT'])
        self.assertEqual(robot.report(), (0, 0, 'NORTH'))

    def test_move(self):
        robot = execute_commands(['PLACE 0,0,NORTH', 'MOVE', 'REPORT'])
        self.assertEqual(robot.report(), (0, 1, 'NORTH'))

    def test_left(self):
        robot = execute_commands(['PLACE 0,0,NORTH', 'LEFT', 'REPORT'])
        self.assertEqual(robot.report(), (0, 0, 'WEST'))

    def test_right(self):
        robot = execute_commands(['PLACE 0,0,NORTH', 'RIGHT', 'REPORT'])
        self.assertEqual(robot.report(), (0, 0, 'EAST'))

    def test_multiple_commands(self):
        robot = execute_commands(['PLACE 1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'REPORT'])
        self.assertEqual(robot.report(), (3, 3, 'NORTH'))

    def test_invalid_place(self):
        robot = execute_commands(['PLACE 5,5,NORTH', 'REPORT'])
        self.assertIsNone(robot.report())

    def test_ignore_invalid_commands_before_place(self):
        robot = execute_commands(['MOVE', 'LEFT', 'REPORT'])
        self.assertIsNone(robot.report())

    def test_prevent_falling(self):
        robot = execute_commands(['PLACE 0,0,SOUTH', 'MOVE', 'REPORT'])
        self.assertEqual(robot.report(), (0, 0, 'SOUTH'))

if __name__ == '__main__':
    unittest.main()


