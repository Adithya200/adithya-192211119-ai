import heapq
import itertools
h6
class PuzzleState:
    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.cost = 0
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __lt__(self, other):
        return (self.cost + self.depth) < (other.cost + other.depth)

    def __str__(self):
        return '\n'.join([str(row) for row in self.puzzle]) + '\n'

    def __hash__(self):
        return hash(str(self.puzzle))

    def goal_state(self, goal):
        return self.puzzle == goal

    def possible_moves(self):
        row, col = self.find_blank()
        possible = []
        if row > 0:
            possible.append(('up', row - 1, col))
        if row < 2:
            possible.append(('down', row + 1, col))
        if col > 0:
            possible.append(('left', row, col - 1))
        if col < 2:
            possible.append(('right', row, col + 1))
        return possible

    def find_blank(self):
        for i, row in enumerate(self.puzzle):
            for j, cell in enumerate(row):
                if cell == 0:
                    return i, j

    def move_blank(self, direction):
        row, col = self.find_blank()
        if direction == 'up' and row > 0:
            self.puzzle[row][col], self.puzzle[row - 1][col] = self.puzzle[row - 1][col], self.puzzle[row][col]
        elif direction == 'down' and row < 2:
            self.puzzle[row][col], self.puzzle[row + 1][col] = self.puzzle[row + 1][col], self.puzzle[row][col]
        elif direction == 'left' and col > 0:
            self.puzzle[row][col], self.puzzle[row][col - 1] = self.puzzle[row][col - 1], self.puzzle[row][col]
        elif direction == 'right' and col < 2:
            self.puzzle[row][col], self.puzzle[row][col + 1] = self.puzzle[row][col + 1], self.puzzle[row][col]

def heuristic(puzzle, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:
                goal_row, goal_col = divmod(puzzle[i][j] - 1, 3)
                h += abs(i - goal_row) + abs(j - goal_col)
    return h

def astar(start, goal):
    count = itertools.count()
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, next(count), start))
    while open_list:
        f, _, state = heapq.heappop(open_list)
        if state.goal_state(goal):
            return state
        closed_list.add(state)
        for move, row, col in state.possible_moves():
            child = PuzzleState([row[:] for row in state.puzzle], state, move)
            child.move_blank(move)
            if child not in closed_list:
                child.cost = heuristic(child.puzzle, goal)
                heapq.heappush(open_list, (child.cost + child.depth, next(count), child))
    return None

def print_steps(solution):
    current = solution
    steps = []
    while current:
        steps.append(current)
        current = current.parent
    steps.reverse()
    for step in steps:
        print(step)

if __name__ == '__main__':
    initial_state = PuzzleState([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    solution = astar(initial_state, goal_state)
    print_steps(solution)
