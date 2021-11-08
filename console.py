#!/usr/bin/python3
'''
'''
import cmd
import models
from models.base_model import BaseModel

dict_of_classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    '''
    '''
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        return True

    def help_quit(self):
        print('Quit command to exit the program')

    def help_EOF(self):
        print('End of file, exits')

    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def do_create(self, args):
        try:
            arguments = args.split()
            if len(arguments) == 0:
                print("** class name missing **")
                return False
            if arguments[0] in dict_of_classes:
                obj = dict_of_classes[arguments[0]]()
            else:
                print("** class doesn't exist **")
                return False
            print(obj.id)
            obj.save()
        except Exception:
            raise

if __name__ == '__main__':
    HBNBCommand().cmdloop()