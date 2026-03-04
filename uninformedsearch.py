from collections import deque

# State: (M_left, C_left, boat_side)
# boat_side: 1 = left, 0 = right
INITIAL = (3, 3, 1)
GOAL    = (0, 0, 0)

MOVES = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # (M, C) moved in boat

def is_valid(m_left, c_left):
    # bounds
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    m_right = 3 - m_left
    c_right = 3 - c_left

    # left side safe
    if m_left > 0 and c_left > m_left:
        return False

    # right side safe
    if m_right > 0 and c_right > m_right:
        return False

    return True

def successors(state):
    m, c, boat = state
    out = []
    for dm, dc in MOVES:
        if boat == 1:  # left -> right
            ns = (m - dm, c - dc, 0)
        else:          # right -> left
            ns = (m + dm, c + dc, 1)

        if is_valid(ns[0], ns[1]):
            out.append(ns)
    return out

def reconstruct_path(parent, end_state):
    path = []
    cur = end_state
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

def pretty_print(path):
    for (mL, cL, boat) in path:
        mR, cR = 3 - mL, 3 - cL
        side = "LEFT " if boat == 1 else "RIGHT"
        print(f"Left({mL},{cL})  Boat:{side}  Right({mR},{cR})")

# ---------------- BFS ----------------
def bfs(start=INITIAL, goal=GOAL):
    q = deque([start])
    parent = {start: None}
    visited = {start}

    expanded = 0
    generated = 1
    max_frontier = 1

    while q:
        max_frontier = max(max_frontier, len(q))
        s = q.popleft()
        expanded += 1

        if s == goal:
            return reconstruct_path(parent, s), expanded, generated, max_frontier

        for ns in successors(s):
            if ns not in visited:
                visited.add(ns)
                parent[ns] = s
                q.append(ns)
                generated += 1

    return None, expanded, generated, max_frontier

# ---------------- DFS ----------------
def dfs(start=INITIAL, goal=GOAL):
    # stack: (state, pathset, parent)
    stack = [(start, {start}, {start: None})]

    expanded = 0
    generated = 1
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        s, pathset, parent = stack.pop()
        expanded += 1

        if s == goal:
            return reconstruct_path(parent, s), expanded, generated, max_frontier

        for ns in successors(s):
            if ns not in pathset:  # avoid cycles in current path
                new_parent = dict(parent)
                new_parent[ns] = s
                stack.append((ns, pathset | {ns}, new_parent))
                generated += 1

    return None, expanded, generated, max_frontier

# -------- Depth-Limited DFS (helper for IDDFS) --------
def dls(start, goal, limit):
    # returns (path, expanded, generated, max_frontier)
    stack = [(start, 0, {start}, {start: None})]  # (state, depth, pathset, parent)

    expanded = 0
    generated = 1
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        s, depth, pathset, parent = stack.pop()
        expanded += 1

        if s == goal:
            return reconstruct_path(parent, s), expanded, generated, max_frontier

        if depth == limit:
            continue

        for ns in successors(s):
            if ns not in pathset:
                new_parent = dict(parent)
                new_parent[ns] = s
                stack.append((ns, depth + 1, pathset | {ns}, new_parent))
                generated += 1

    return None, expanded, generated, max_frontier

# ---------------- IDDFS ----------------
def iddfs(start=INITIAL, goal=GOAL, max_depth=30):
    total_expanded = 0
    total_generated = 0
    overall_max_frontier = 0

    for limit in range(max_depth + 1):
        path, expanded, generated, max_frontier = dls(start, goal, limit)

        total_expanded += expanded
        total_generated += generated
        overall_max_frontier = max(overall_max_frontier, max_frontier)

        if path is not None:
            return path, total_expanded, total_generated, overall_max_frontier, limit

    return None, total_expanded, total_generated, overall_max_frontier, None

def run_all(max_iddfs_depth=30):
    print("=== Missionaries & Cannibals (3,3) — BFS vs DFS vs IDDFS ===\n")

    # BFS
    path, exp, gen, mf = bfs()
    print("BFS:")
    if path:
        print(f"  Moves: {len(path)-1} (shortest guaranteed)")
        print(f"  Expanded={exp}, Generated={gen}, MaxFrontier={mf}")
        pretty_print(path)
    else:
        print("  No solution found.")
    print()

    # DFS
    path, exp, gen, mf = dfs()
    print("DFS:")
    if path:
        print(f"  Moves: {len(path)-1} (NOT guaranteed shortest)")
        print(f"  Expanded={exp}, Generated={gen}, MaxFrontier={mf}")
        pretty_print(path)
    else:
        print("  No solution found.")
    print()

    # IDDFS
    path, exp, gen, mf, found_limit = iddfs(max_depth=max_iddfs_depth)
    print(f"IDDFS (max depth tried = {max_iddfs_depth}):")
    if path:
        print(f"  Found at depth limit = {found_limit}")
        print(f"  Moves: {len(path)-1} (shortest in edges, like BFS, for unit costs)")
        print(f"  TotalExpanded={exp}, TotalGenerated={gen}, MaxFrontier={mf}")
        pretty_print(path)
    else:
        print("  No solution found within max depth.")
        print(f"  TotalExpanded={exp}, TotalGenerated={gen}, MaxFrontier={mf}")
    print()

if __name__ == "__main__":
    run_all(max_iddfs_depth=30)