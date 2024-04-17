from typing import TypeVar, Generic

T = TypeVar('T', int, float)


class Pair(Generic[T]):
    def __init__(self, left: T, right: T):
        self.left = left
        self.right = right



def main():
    pair = Pair(10, 10)
    print(pair.left, pair.right)



if __name__ == '__main__':
    main()
