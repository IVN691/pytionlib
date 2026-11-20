import re

class Action:
    def __init__(self, func, *args):
        self.func = func
        self.args = args
        self.used = False

    def run(self):
        self.used = True
        self.func(*self.args)

    def __del__(self):
        if not self.used:
            self.run()

def say(str=""):
    return Action(print, str)

def repeat(action="", num=0):
    if not isinstance(action, Action):
        raise TypeError("Acction command expected")

    action.used = True

    for i in range(num):
        action.run()

def math(x=""):
    if not isinstance(x, str):
        return x
    if not re.fullmatch(r"[0-9+\-*/%.()\s]+", x):
        raise ValueError("Only math characters allowed")
    return eval(x, {"__builtins__": {}}, {})