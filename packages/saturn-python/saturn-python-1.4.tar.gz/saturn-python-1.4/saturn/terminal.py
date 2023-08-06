"""
Terminal implements a command line where you can rerun a module and manage
the scope.
"""

import os
import sys
import traceback
from importlib import reload

try:
    import readline
except ModuleNotFoundError:
    pass

from .version import __version__
from .scope import Scope


class Terminal:
    welcome = "Welcome to Saturn terminal where you can reruns " \
              "your Python module keeping its scope in RAM. " \
              "Version {}.".format(__version__)
    prompt = "S>>> "

    def __init__(self):
        # Dictionaly to store imported modules
        self._modules = {}

    def run(self):
        # Define empty scope
        scope = Scope()

        # Print welcome
        print(self.welcome)

        # Terminal loop
        while True:
            # Wait for a command
            command = input(self.prompt).strip()

            # Skip if the command is empty
            if not command:
                continue

            # Exit
            elif command == "exit":
                break

            # Run module
            elif command.startswith("run "):
                # Parse command arguments
                try:
                    module_name, section = self._parse_run_args(command[4:])
                except ValueError as exc:
                    print("Error:", exc.args[0])
                    continue

                # Set saturn section
                self._set_section(section)

                # Run target function in the module
                self._run_module(module_name, scope)

            # Execute a python expression
            else:
                try:
                    exec(command, {'scope': scope})
                except BaseException:
                    traceback.print_exc()

    def _run_module(self, module_name, scope):
        # Catch all exceptions (including syntax and keyboard interruptions)
        try:
            # Import or reload the module
            if module_name not in self._modules:
                self._modules[module_name] = __import__(module_name)
            else:
                reload(self._modules[module_name])

            # Get target to run
            target = __import__('saturn').target

            # Run with the scope
            target(scope)

        except BaseException:
            traceback.print_exc()

    def _parse_run_args(self, args_str):
        """
        This function parses argument string for run command and returns
        the module name and section. If no section is set, it returns None.
        """
        # Split argument string
        parts = args_str.strip().split()

        # If a module name is given only, return it with empty section
        if len(parts) == 1:
            return parts[0], None

        # If both are provided, return them
        elif len(parts) == 2:
            return parts[0], parts[1]

        # Raise exception if there are too many arguments
        else:
            raise ValueError("too many arguments for run command")

    def _set_section(self, section):
        # Set SATURN_SECTION environment variable
        if section is not None:
            os.environ['SATURN_SECTION'] = section
        else:
            os.environ.pop('SATURN_SECTION', None)


def main():
    # Add path of the run script to sys.path
    sys.path.append(os.getcwd())

    # Create and run terminal
    terminal = Terminal()
    terminal.run()
