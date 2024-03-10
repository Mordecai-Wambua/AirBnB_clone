#!/usr/bin/python3
"""Actual python terminal."""


import cmd
import models
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter."""

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"
    ruler = '='
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
               'Review']

    def do_create(self, line):
        """Create new BaseModel instance.

        Args:
            line: the class name
        """
        parts = line.split()

        if not parts:
            print("** class name missing **")
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        else:
            print(eval(parts[0])().id)
            storage.save()

    def do_show(self, line):
        """Print the string representation of an instance.

        Args:
            line: the class name
        """
        parts = line.split()
        if not parts:
            print("** class name missing **")
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(parts) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(parts[0], parts[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(parts[0], parts[1])])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id.

        Args:
            line: the class name
        """
        parts = line.split()
        if not parts:
            print("** class name missing **")
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(parts) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(parts[0], parts[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(parts[0], parts[1])]
            storage.save()

    def do_all(self, line):
        """Print all string rep of  instances based on the class name."""
        parts = line.split()
        output = []
        if not parts:
            for instance in storage.all().values():
                output.append(str(instance))
            print(output)
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        else:
            for instance in storage.all().values():
                if instance.__class__.__name__ == parts[0]:
                    output.append(str(instance))
                print(output)

    def do_update(self, line):
        """Update an instance based on the class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        parts = line.split()
        if not parts:
            print("** class name missing **")
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(parts) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(parts[0], parts[1]) not in storage.all():
            print("** no instance found **")
        elif len(parts) < 3:
            print("** attribute name missing **")
        elif len(parts) < 4:
            print("** value missing **")
        else:
            name = parts[2]
            value = parts[3]
            instance = storage.all()["{}.{}".format(parts[0], parts[1])]
            setattr(instance, name, value)
            storage.save()

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Define action performed incase of empty line input."""
        pass

    def do_EOF(self, line):
        """Allow the program to exit cleanly."""
        return True

    def postloop(self):
        """Acts when cmdloop is about to return."""
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
