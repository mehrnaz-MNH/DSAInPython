def isValid(self, s: str) -> bool:
    char_stack = []

    for c in s:
        if c in '([{':
            char_stack.append(c)

        elif c in ')]}':
            if len(char_stack) == 0:
                return False
            top = char_stack.pop()
            if top == '(' and c != ')' or top == '[' and c != ']' or top == '{' and c != '}':
                return False

    return len(char_stack) == 0