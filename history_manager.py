class HistoryManager:
    def __init__(self, max_steps=10):
        self.undo_stack = []
        self.redo_stack = []
        self.max_steps = max_steps

    def SaveState(self, image):
         if image is not None:
           self.undo_stack.append(image.copy())

           if len(self.undo_stack) > self.max_steps:
            self.undo_stack.pop(0)

           self.redo_stack.clear()

    def Undo(self):
        if len(self.undo_stack) > 1:
          last_state = self.undo_stack.pop()
          self.redo_stack.append(last_state)
          return self.undo_stack[-1]

        return None

    def Redo(self):
        if self.redo_stack:
          state = self.redo_stack.pop()
          self.undo_stack.append(state)
          return state

        return None

    def ClearHistory(self):
        self.undo_stack.clear()
        self.redo_stack.clear()