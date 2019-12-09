from collections import defaultdict

class Node:

    def __init__(self, name, parent):
        
        self.name = name
        if parent is None:
            self.dfc = 0
            self.parents = []
        else:
            self.dfc = parent.dfc + 1
            self.parents = parent.parents + [parent]

    def __repr__(self):
        return f'{self.name}'


def read_and_sort(filename='input_7.txt'):
    lines = open(filename).readlines()
    broken_lines = [l.strip().split(')') for l in lines]
    parent_child_dict = defaultdict(list)

    for parent, kid in broken_lines:
        parent_child_dict[parent].append(kid)

    return parent_child_dict

def build_tree(parent_child_dict):

    root = Node('COM', None)
    nodes_to_processs = [root]
    total_dfc_count = 0
    santa = None
    you = None
    while nodes_to_processs:
        current_node = nodes_to_processs.pop(0)
        if current_node.name == 'SAN': santa = current_node
        if current_node.name == 'YOU': you = current_node
        total_dfc_count += current_node.dfc
        c_of_current_node = parent_child_dict[current_node.name]

        for c in c_of_current_node:
            nodes_to_processs.append(Node(name=c, parent=current_node))

    return root, total_dfc_count, santa, you

root, total_dfc_count, santa, you = build_tree(read_and_sort())

def common_ancestor(santa, you):
    for s_parent, y_parent in zip(santa.parents, you.parents):
        if s_parent != y_parent:
            return s_parent.parents[-1]

lce = common_ancestor(santa, you)

print((santa.dfc - lce.dfc) + (you.dfc - lce.dfc) - 2)
    


