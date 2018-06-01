"""
Finds strongly connected components (SCCs) in a directed graph.
A single DFS pass is used to identify SCCs based on discovery and low-link values.
"""


def tarjan_scc(n, adj):
    ids, low = [-1] * n, [0] * n
    on_stack = [False] * n
    stack, res = [], []
    timer = 0

    def dfs(at):
        nonlocal timer
        stack.append(at)
        on_stack[at] = True
        ids[at] = low[at] = timer
        timer += 1
        for to in adj[at]:
            if ids[to] == -1:
                dfs(to)
                low[at] = min(low[at], low[to])
            elif on_stack[to]:
                low[at] = min(low[at], ids[to])
        if ids[at] == low[at]:
            component = []
            while stack:
                node = stack.pop()
                on_stack[node] = False
                low[node] = ids[at]
                component.append(node)
                if node == at:
                    break
            res.append(component)

    for i in range(n):
        if ids[i] == -1:
            dfs(i)
    return res
