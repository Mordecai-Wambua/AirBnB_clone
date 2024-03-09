#!/usr/bin/python3
"""Actual python terminal."""


import cmd
import json
from shlex import split
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter."""

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"
    ruler = '='
    classes = ['BaseModel']

    def do_create(self, line):
        """Create new BaseModel instance.

        Args:
            line: the class name
        """
        parts = line.split()

        if not parts:
            print("** class name missing **")
            return
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
            return
        else:
            print(eval(parts[0])().id)
            storage.save()


    def do_show(self, line):
        """Prints the string representation of an instance.

        Args:
            line: the class name
        """
        parts = line.split()
        
        if not parts:
            print("** class name missing **")
            return
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
            return
        elif len(parts) < 2:
            print("** instance id missing **")
            return

        identifier = "{}.{}".format(parts[0], parts[1])
        if identifier not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[identifier])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.

        Args:
            line: the class name
        """
        parts = line.split()
        if not parts:
            print("** class name missing **")
            return
        elif parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
            return
        elif len(parts) < 2:
            print("** instance id missing **")
            return
        identifier = "{}.{}".format(parts[0], parts[1])
        if identifier not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[identifier]
        storage.save()

    def do_all(self, line):
        """Prints all string rep of  instances based on the class name."""
        parts = line.split()
        output = []
        if not parts:
            for instance in storage.all().values():
                output.append(str(instance))
                print(output)
                return
        if parts[0] not in self.__class__.classes:
            print("** class doesn't exist **")
            return
        for instance in storage.all().values():
            if instance.__class__.__name__ == parts[0]:
                output.append(str(instance))
        print(output)


    def do_update(self, line):
        """Updates an instance based on the class name and id.
        
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        pass     


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
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
