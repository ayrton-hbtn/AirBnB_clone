# AirBnB_clone

*This is the first part of the AirBnB clone project for Holbertonschool: The console.*

## Description

This program contains all the classes needed to store data (User, State, City, Place, Amenity, Review) that inherit from BaseModel. The data is handled by class FileStorage, goes through a flow of JSON serialization/deserialization:

<class 'custom'> **->** to_dict() **->** <class 'dict'> **->** JSON dump **->** <class 'str'> **->** FILE **->** <class 'str'> **->** JSON load **->** <class 'dict'> **->** <class 'custom'>


 #### class FileStorage:
> ##### Private attributes:
> - __file_path: string - path to the JSON file (ex: file.json)
> - __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
>    
> ##### Public instance methods:
> - all(self): returns the dictionary __objects
> - new(self, obj): sets in __objects the obj with key <obj class name>.id
> - save(self): serializes __objects to the JSON file (path: __file_path)
> - reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)    

## Console

Command interpreter to manipulate the data mentioned above. Uses the Python's cmd module.

#### List of commands available:

> - quit & EOF: used to exit the program
> - create: Creates a new instance of a custom class, saves it (to the JSON file) and prints the id
> - show: Prints the string representation of an instance based on the class name and id
> - destroy: Deletes an instance based on the class name and id (save the change into the JSON file)
> - all: Prints all string representation of all instances based or not on the class name
> - update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
> - empty line + ENTER: does nothing
> - help: Shows basic info about every command
> ##### Rules:
> - You can assume arguments are always in the right order
> - Each arguments are separated by a space
> - A string argument with a space must be between double quote
> - The error management starts from the first argument to the last one

#### Colaborators:
 - [Ayrton Coelho](https://github.com/hippocampus3282)
 - [Sebastian Moreira](https://github.com/GuzhiRegem)