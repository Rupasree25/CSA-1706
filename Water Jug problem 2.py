from collections import deque
capacity = (12, 8, 5)
start = (12, 0, 0)
queue = deque([(start, [])])
visited = {start}
while queue:
    state, path = queue.popleft()
    if 6 in state:
        for step in path + [state]:
            print(step)
        print("Target of 6 litres reached!")
        break
    for i in range(3):
        for j in range(3):
            if i != j:
                amount = min(state[i], capacity[j] - state[j])
                if amount > 0:
                    new_state = list(state)
                    new_state[i] -= amount
                    new_state[j] += amount
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [state]))
