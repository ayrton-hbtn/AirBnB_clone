#!/usr/bin/python3
'''
'''
import cmd
from models import storage
from models.engine import classes

class HBNBCommand(cmd.Cmd):
    '''
    '''
    prompt = "(hbnb) "

    def do_EOF(self, line):
        '''End of file, exits'''
        return True
    
    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def do_create(self, args):
        ''' create '''
        try:
            arguments = args.split()
            if len(arguments) == 0:
                print("** class name missing **")
                return False
            if arguments[0] in classes:
                obj = classes[arguments[0]]()
            else:
                print("** class doesn't exist **")
                return False
            print(obj.id)
            obj.save()
        except Exception:
            raise

    def do_show(self, args):
        ''' show an instance '''
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arguments) < 2:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(arguments[0], arguments[1])
        st = storage.all()
        if key not in st:
            print("** no instance found **")
            return False
        print(st[key])

    def do_all(self, args):
        ''' Prints all string representation of all instances based '''
        arguments = args.split()
        if len(arguments) == 0:
            for key, value in storage.all().items():
                print(value)
            return False
        class_n = arguments[0]
        if class_n not in classes:
                print("** class doesn't exist **")
                return False
        for key, value in storage.all().items():
            if key.startswith(class_n):
                print(value)

    def do_destroy(self, args):
        ''' destroy '''
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arguments) < 2:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(arguments[0], arguments[1])
        if key not in storage.all():
            print("** no instance found **")
            return False
        storage.delete(key)

    def do_update(self, args):
        ''' update '''
        arguments = args.split()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
