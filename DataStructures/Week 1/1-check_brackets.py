# python3

from collections import deque


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    
    stack = deque()
    opens = ["(", "[", "{"]
    closed = [")", "]", "}"]
    text = list(text)
    i = 0
    while i < len(text):
        #Ignore non brackets
        if text[i] not in opens and text[i] not in closed:
            i += 1
            continue
        if text[i] in opens:
            #Store the index of the open bracket
            stack.append(i)
            i+= 1
            continue
        #If there is a closing bracket and no open bracket in the stack, return 
        if len(stack) == 0: return i + 1
        top = stack.pop()
        if not are_matching(text[top], text[i]): return i + 1
        i += 1
        
    if len(stack) == 0: return "Success"
    else: return stack.popleft() + 1

    
if __name__ == "__main__":
    # print(find_mismatch("[](()"))
    text = input()
    print(find_mismatch(text))
