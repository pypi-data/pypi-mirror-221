import os

from .version import __version__


# Reference to the main function that will be rerun in the daemon.
target = None


def main(func):
    """
    A decorator that registers the main function.

    Example:

        @saturn.main
        def main():
            ...
    """
    global target
    target = func
    return func


def defined(expr, scope):
    """
    Check if a variable is already defined in the scope.
    """
    try:
        eval(expr, {'scope': scope})
    except AttributeError:
        return False
    else:
        return True


def safe(expr, scope):
    """
    Safe run the expression that returns None if an error comes.
    """
    try:
        return eval(expr, {'scope': scope})
    except:
        return None


def section(label):
    """
    Returns True if the passed label is equal to the section value
    that is set in run command else False.
    If nothing is passed as section in run command, the function returns True.
    """
    saturn_section = os.environ.get('SATURN_SECTION')
    return saturn_section is None or saturn_section == str(label)
