#!/usr/bin/python3
"""this module contains the program console.py that contains
the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """class definition"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """exits the program"""

        return True

    def do_EOF(self, line):
        """exits the program"""

        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
