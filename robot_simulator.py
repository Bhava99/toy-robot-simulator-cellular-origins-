class ToyRobotSimulator:
    DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.placed = False

    def place(self, x, y, facing):
        if 0 <= x <= 4 and 0 <= y <= 4 and facing in self.DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing
            self.placed = True

    def move(self):
        if not self.placed:
            return
        if self.facing == 'NORTH' and self.y < 4:
            self.y += 1
        elif self.facing == 'EAST' and self.x < 4:
            self.x += 1
        elif self.facing == 'SOUTH' and self.y > 0:
            self.y -= 1
        elif self.facing == 'WEST' and self.x > 0:
            self.x -= 1

    def left(self):
        if not self.placed:
            return
        self.facing = self.DIRECTIONS[(self.DIRECTIONS.index(self.facing) - 1) % 4]

    def right(self):
        if not self.placed:
            return
        self.facing = self.DIRECTIONS[(self.DIRECTIONS.index(self.facing) + 1) % 4]

    def report(self):
        if not self.placed:
            return None
        return self.x, self.y, self.facing

def execute_commands(commands):
    robot = ToyRobotSimulator()
    for command in commands:
        if not command.strip():  # Skip empty commands
            continue
        parts = command.split()
        if parts[0] == 'PLACE' and len(parts) == 2:
            x, y, f = parts[1].split(',')
            robot.place(int(x), int(y), f)
        elif parts[0] == 'MOVE':
            robot.move()
        elif parts[0] == 'LEFT':
            robot.left()
        elif parts[0] == 'RIGHT':
            robot.right()
        elif parts[0] == 'REPORT':
            position = robot.report()
            if position:
                print(f"{position[0]},{position[1]},{position[2]}")
    return robot

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            commands = file.readlines()
            commands = [command.strip() for command in commands]
            execute_commands(commands)
    else:
        while True:
            command = input().strip()
            if command == 'EXIT':
                break
            execute_commands([command])
