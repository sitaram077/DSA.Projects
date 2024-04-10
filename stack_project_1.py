"""Checks if a string has balanced parentheses."""
def is_balanced(expr):
  stack = []
  opening_parens = ["(", "[", "{"]
  closing_parens = [")", "]", "}"]
  for char in expr:
    if char in opening_parens:
      stack.append(char)
    elif char in closing_parens:
      i=stack.pop()
      if stack and opening_parens[i] == char:
        continue
      else:
        return False
  return len(stack) == 0

# Example usage
expression = "(a + b) * c"
if is_balanced(expression):
  print("Expression is balanced")
else:
  print("Expression is unbalanced")
