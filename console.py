#!/usr/bin/python3
"""this module contains the program console.py that contains
the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""

        if len(arg) == 0:
            print("** class name missing **")
        elif arg in classes:
            new_instance = eval(arg + '()')
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id"""

        if len(arg) == 0:
            print("** class name missing **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
