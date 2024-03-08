from collections import deque
jug1_capacity = 4
jug2_capacity = 3
goal_amount = 2
initial_state = (0, 0)
actions = [
    ("Fill Jug 1", lambda state: (jug1_capacity, state[1])),
    ("Fill Jug 2", lambda state: (state[0], jug2_capacity)),
    ("Empty Jug 1", lambda state: (0, state[1])),
    ("Empty Jug 2", lambda state: (state[0], 0)),
    ("Pour Jug 1 to Jug 2", lambda state: (
        max(0, state[0] - (jug2_capacity - state[1])),
        min(jug2_capacity, state[1] + state[0]))
     ),
    ("Pour Jug 2 to Jug 1", lambda state: (
        min(jug1_capacity, state[0] + state[1]),
        max(0, state[1] - (jug1_capacity - state[0])))
     )
]


def water_jug_problem(initial_state, goal_amount):
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        current_state, actions_taken = queue.popleft()
        if current_state[0] == goal_amount or current_state[1] == goal_amount:
            return actions_taken
        visited.add(current_state)
        for action_name, action_func in actions:
            new_state = action_func(current_state)
            if new_state not in visited:
                new_actions_taken = actions_taken + [action_name]
                queue.append((new_state, new_actions_taken))
                visited.add(new_state)
    return "No solution found"
if __name__ == "__main__":
    solution = water_jug_problem(initial_state, goal_amount)
    if solution:
        print("Solution found:")
        for action in solution:
            print(action)
    else:
        print("No solution exists.")