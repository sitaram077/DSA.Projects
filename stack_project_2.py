def precedence(op):
  """Returns the precedence of an operator."""
  if op in "+-":
    return 1
  elif op in "*/":
    return 2
  else:
    return 0


def infix_to_postfix(expr):
    """Converts infix expression to postfix notation."""
    stack = []
    postfix = []
    operand = ''
    for char in expr:
        if char == ' ':
            continue
        if char.isalnum():
            operand += char
        else:
            if operand:
                postfix.append(operand)
                operand = ''
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack:
                    stack.pop()  # Pop the '(' if it exists
                else:
                    # Handle mismatched parentheses
                    raise ValueError("Mismatched parentheses")
            else:
                while stack and precedence(stack[-1]) >= precedence(char):
                    postfix.append(stack.pop())
                stack.append(char)
    if operand:
        postfix.append(operand)
    while stack:
        if stack[-1] == '(':
            # Handle mismatched parentheses
            raise ValueError("Mismatched parentheses")
        postfix.append(stack.pop())
    return " ".join(postfix)

# Example usage
expression = "(a + b) * c"
postfix_expr = infix_to_postfix(expression)
print("Postfix expression:", postfix_expr)


