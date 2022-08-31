#python3
import sys

class GivenSolution():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = 0

    def Push(self, a):
        self.__stack.append(a)
        if a > self.__max:
            self.__max = a

    def Pop(self):
        assert(len(self.__stack))
        val = self.__stack.pop()
        if val == self.__max:
            self.__max = max(self.__stack)

    def Max(self):
        assert(len(self.__stack))
        return self.__max

if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(input("Num queries: "))
    for i in range(num_queries):
        query = input(f"Query {i + 1}: ").split()
        
    # num_queries = int(sys.stdin.readline())
    # for _ in range(num_queries):
    #     query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
