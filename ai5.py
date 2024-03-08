from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if self.missionaries > self.cannibals and self.missionaries < 3:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f'M({self.missionaries}) C({self.cannibals}) B({self.boat})'

def successors(state):
    children = []
    if state.boat == 1:
        children.extend([State(state.missionaries - i, state.cannibals - j, 0)
                         for i in range(3) for j in range(3) if 1 <= i + j <= 2])
    else:
        children.extend([State(state.missionaries + i, state.cannibals + j, 1)
                         for i in range(3) for j in range(3) if 1 <= i + j <= 2])
    return [child for child in children if child.is_valid()]

def breadth_first_search(initial_state):
    visited = set()
    queue = deque([[initial_state]])

    while queue:
        path = queue.popleft()
        state = path[-1]

        if state.is_goal():
            return path

        for successor in successors(state):
            if successor not in visited:
                visited.add(successor)
                new_path = list(path)
                new_path.append(successor)
                queue.append(new_path)

    return None

def print_solution(solution):
    for state in solution:
        print(state)

def main():
    initial_state = State(3, 3, 1)
    solution = breadth_first_search(initial_state)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
