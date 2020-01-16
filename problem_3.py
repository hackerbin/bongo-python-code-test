class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node_a, node_b):
    if not (isinstance(node_a, Node) and isinstance(node_b, Node)):
        raise ValueError("Nodes must be Node object")
    ancestors = {}
    while node_a:
        ancestors[node_a.value] = 1
        node_a = node_a.parent

    while node_b:
        if node_b.value in ancestors.keys():
            print(node_b.value)
            return node_b
        node_b = node_b.parent
    return None


node1 = Node(1, None)
node2 = Node(2, node1)
node3 = Node(3, node1)
node4 = Node(4, node2)
node5 = Node(5, node2)
node6 = Node(6, node3)
node7 = Node(7, node3)
node8 = Node(8, node4)
node9 = Node(9, node4)

lca_node = lca(node7, node7)
if lca_node:
    print(lca_node.value)
