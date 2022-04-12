"""
@Time : 2022/4/12 16:21
@Author : Tianqi Tang
@File : stack.py
@IDE : PyCharm
"""


class MyStack(object):
    def __init__(self):
        super(MyStack, self).__init__()
        self.lists = []
        self.length = 0

    def push(self, val):
        self.lists.append(val)
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("The Stack is empty")
        else:
            self.lists.pop(self.length - 1)
            self.length -= 1

    def top(self):
        if self.length == 0:
            return None
        else:
            return self.lists[self.length - 1]


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(2)
    print(myStack.top())
    myStack.push(4)
    print(myStack.top())
    myStack.pop()
    print(myStack.top())
    myStack.pop()
    print(myStack.top())
