0x00. AirBnB clone - The console
# AirBnB Clone

This project is a command interpreter for an Airbnb clone application. It is built using Python and focuses on creating a data model to manage the backend of the application.

## Description

The AirBnB clone is a complete web application that integrates a database to manage the backend data, a front-end to display it, and an API to allow external services to interact with the application. This repository contains the first step of the project, which is to create the data model and the command interpreter.

The data model is a hierarchical mapping of JSON objects, where each object represents one of the following entities:

- **BaseModel**: The base class for all other classes.
- **User**: Represents a user of the application.
- **State**: Represents a state or region.
- **City**: Represents a city within a state.
- **Amenity**: Represents an amenity that can be added to a place.
- **Place**: Represents a physical location, such as a house or an apartment.
- **Review**: Represents a review of a place.

The command interpreter allows you to create, update, and manage objects of these classes through a command-line interface.

## Command Interpreter

### Starting the Command Interpreter

To start the command interpreter, navigate to the project directory and run the following command:

This will open the command prompt `(hbnb)`.

### Using the Command Interpreter

The command interpreter supports the following commands:

- `create <class>`: Create an instance of the specified class.
- `show <class> <id>`: Display the string representation of an instance.
- `destroy <class> <id>`: Delete an instance from the storage.
- `all <class>`: Display all instances of the specified class.
- `update <class> <id> <attribute_name> <attribute_value>`: Update an instance of the specified class.
- `quit` or `EOF`: Exit the command interpreter.
- `help`: Display the available commands.

### Examples

Create a new `User` instance:

## Authors

This project is part of the curriculum at Holberton School. The authors who contributed to this project are listed in the [AUTHORS](AUTHORS) file.

# This file lists all individuals having contributed content to the repository.

Your Name <livingstoneamisi00@gmail.com>
Collaborator 1 <mordecaingumbau@gmail.com>
