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

def nested_list_to_tuple(nested_list):
    if isinstance(nested_list, list):
        return tuple(nested_list_to_tuple(item) for item in nested_list)
    return nested_list