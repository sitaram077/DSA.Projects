class Action:
  def __init__(self, data, action_type):
    self.data = data
    self.action_type = action_type  # "insert" or "delete"

  def undo(self, text):
    if self.action_type == "insert":
      text.pop()
    elif self.action_type == "delete":
      text.append(self.data)

class TextEditor:
  def __init__(self):
    self.text = []
    self.undo_stack = []

  def insert(self, char):
    self.text.append(char)
    self.undo_stack.append(Action(char, "insert"))

  def delete(self):
    if self.text:
      char = self.text.pop()
      self.undo_stack.append(Action(char, "delete"))

  def undo(self):
    if self.undo_stack:
      action = self.undo_stack.pop()
      action.undo(self.text)

  def redo(self):
      pass
    # Implement redo functionality (optional)

# Example usage
editor = TextEditor()
editor.insert("h")
editor.insert("e")
editor.insert("l")
editor.delete()
print(editor.text)  # Output: ["h", "e"]

editor.undo()
print(editor.text)  # Output: ["h", "e", "l"]
