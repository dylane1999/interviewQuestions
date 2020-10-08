from collections import deque


def superStack(operations):
    myStack = deque()
    for i in range(len(operations)):
        l = operations[i].split(' ')
        if l[0] == "push":
            myStack.append(l[1])
            print(myStack[-1])
        if l[0] == "pop":
            if myStack:
                myStack.pop()
                if myStack:
                    print(myStack[-1])
                else:
                    print("EMPTY")
            else:
                print("EMPTY")
        if l[0] == "inc":
            if myStack:
                elementsToAdd = int(l[1])
                valueToadd = int(l[2])
                for i in range(int(elementsToAdd)):
                    element = int(myStack[i])
                    myStack[i] = int(element + valueToadd)
                print(myStack[-1])
            else:
                print("EMPTY")



def
