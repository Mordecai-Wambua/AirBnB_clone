#!/usr/bin/python3
"""Actual python terminal."""


import cmd
class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter."""

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

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
