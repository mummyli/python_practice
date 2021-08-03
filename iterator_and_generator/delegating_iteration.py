class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._children = []

    def __repr__(self) -> str:
        return "Node {!r} ".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    # 返回实现了 __next__()方法的迭代对象
    def __iter__(self):
        return iter(self._children)


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print(ch)