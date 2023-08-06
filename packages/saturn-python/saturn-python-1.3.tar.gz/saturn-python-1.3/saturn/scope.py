"""
A scope object that stores python variables between daemon runs.
The access to the variables is implemented as attributes.
"""

class Scope:
    def __repr__(self):
        return repr(self.__dict__)

    def __contains__(self, name):
        return name in self.__dict__

    def clear(self):
        self.__dict__.clear()
