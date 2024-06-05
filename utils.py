def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

class InterpreterError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)