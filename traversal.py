def dfs(node):
    if node:
        node.color = "blue"
        dfs(node.left)
        dfs(node.right)