def find_errors(tree_description):
    import re
    from collections import defaultdict, deque

    # Parse input
    pairs = re.findall(r'\((\w),(\w)\)', tree_description)
    children = defaultdict(list)
    parent_map = {}
    node_set = set()

    for parent, child in pairs:
        node_set.add(parent)
        node_set.add(child)
        # E2: Duplicate parent-child pair
        if child in children[parent]:
            return "E2"
        children[parent].append(child)
        # E3: More than one parent
        if child in parent_map:
            return "E3"
        parent_map[child] = parent

    # E1: More than two children for any node
    for parent, kids in children.items():
        if len(kids) > 2:
            return "E1"

    # Find root(s)
    root_candidates = node_set - parent_map.keys()
    # E4: Multiple roots
    if len(root_candidates) != 1:
        return "E4"
    root = next(iter(root_candidates))

    # Check for cycles and validate the tree structure
    visited = set()
    stack = [(root, None)]

    while stack:
        node, parent = stack.pop()
        if node in visited:
            # E5: Cycle detected
            return "E5"
        visited.add(node)
        for child in children[node]:
            if child != parent:
                stack.append((child, node))

    # If no errors found, return nothing
    return ""


# Example usage
tree_description = "(A,B) (B,C) (A,E) (B,D)"
print(find_errors(tree_description))  # Should print nothing, meaning no errors

# Additional test case
tree_description_with_errors = "(A,B) (A,B) (B,C) (A,E) (B,D)"
print(find_errors(tree_description_with_errors))  # Should print "E2"
