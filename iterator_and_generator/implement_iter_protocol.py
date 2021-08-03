class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._children = []

    def __repr__(self) -> str:
        return "Node({!r})".format(self._value)

    def __iter__(self):
        return iter(self._children)

    def add_child(self, node):
        self._children.append(node)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)

child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for c in root.depth_first():
    print(c)