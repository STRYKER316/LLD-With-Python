from typing import TypeVar, Generic

T = TypeVar('T')
V = TypeVar('V')

class Pair(Generic[T, V]):
    def __init__(self, left: T, right: V):
        self.left = left
        self.right = right


def main():
    pair = Pair(10, "Hello")
    print(pair.left, pair.right)


if __name__ == '__main__':
    main()
