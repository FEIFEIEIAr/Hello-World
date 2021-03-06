# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i, next))

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack == []:
                return i + 1
            top = opening_brackets_stack.pop()
            if are_matching(top[1], next):
                continue
            else:
                return i + 1
    if opening_brackets_stack == []:
        return True
    else:
        return opening_brackets_stack[0][0] + 1

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch is True:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
