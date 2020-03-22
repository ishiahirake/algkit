import json


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build(data):
    """Build a binary tree using the leetcode data format.

    TODO Add description for leetcode data format.

    :param str|list data:
    :return: root node of the binary tree.
    """
    values = json.loads(data) if isinstance(data, str) else data
    if not values:
        return None

    root = TreeNode(values[0])

    _fill_tree([root], values[1:])

    return root


def _fill_tree(nodes: list, values: list):
    if not values:
        return []

    leafs = []
    count = min(len(nodes) * 2, len(values))

    for i in range(count):
        node = None if values[i] is None else TreeNode(values[i])
        parent = nodes[i // 2]
        if i % 2 == 0:
            parent.left = node
        else:
            parent.right = node
        if node is not None:
            leafs.append(node)

    _fill_tree(leafs, values[count:])


def preorder(root, initial: list = None):
    """
    Preorder traverse binary tree and return value as list.

    :param TreeNode|None root:
    :param list|None initial: initial value of the value list, default to empty list.
    :return: preorder value list
    """
    if initial is None:
        initial = []
    if not root:
        return initial
    initial.append(root.val)
    preorder(root.left, initial)
    preorder(root.right, initial)

    return initial
