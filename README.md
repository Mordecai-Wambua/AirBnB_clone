# AirBnB Clone Project

Welcome to our AirBnB clone project!

## Description

This project aims to create a command-line interpreter for managing AirBnB objects. It involves implementing a parent class (BaseModel) for initialization, serialization, and deserialization of instances, as well as creating a flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.

## Command Interpreter

### How to Start

To start the command interpreter, run the following command:

```bash
$ ./console.py

## Usage
In the interactive mode, you can use commands like:

- (hbnb) help
- (hbnb) create User
- (hbnb) show User 1234-5678
- (hbnb) update User 1234-5678 first_name "John"
- (hbnb) all
- (hbnb) destroy User 1234-5678
- (hbnb) quit

In non-interactive mode, you can use:

$ echo "help" | ./console.py

## Examples
Creating a User:

- (hbnb) create User

Showing all objects:

(hbnb) all
