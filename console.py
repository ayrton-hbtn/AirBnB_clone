#!/usr/bin/python3
'''Console to manage program objects and data
'''
import cmd
from models import storage
from models.engine import classes


def count_class(st):
    """ count amount of <class(st)> instances """
    args = st.split()
    out = 0
    for a in storage.all():
        if a.startswith(args[0]):
            out += 1
    print(out)


class HBNBCommand(cmd.Cmd):
    '''Console to manipulate all the objects in the program
    '''
    prompt = "(hbnb) "

    def default(self, arg):
        '''default method '''
        fun_dict = {
            "all": self.do_all,
            "count": count_class,
            "show": self.do_show,
            "create": self.do_create,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        args = arg.split(".", 1)
        f_class = args[0]
        if (f_class in classes) and len(args) >= 2:
            args = "".join(args[1:]).split("(")
            f_func = args[0]
            if (f_func in fun_dict) and len(args) >= 2:
                f_args = " ".join(tuple("".join(args[1:])[:-1].split(", ")))
                fun_dict[f_func]("{} {}".format(f_class, f_args))
                return False
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, line):
        '''End of file, exits'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        '''Empty line in the cmd, does nothing '''
        pass

    def do_create(self, args):
        '''Command to create a new instance of class '''
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
        '''Shows an instance of class '''
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
        '''Prints string representation of all instances stored '''
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
        '''Destroys an instance '''
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
        '''Updates instance attributes '''
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
        if len(arguments) < 3:
            print("** attribute name missing **")
            return False
        if len(arguments) < 4:
            print("** value missing **")
            return False
        setattr(storage.all()[key], arguments[2], arguments[3])
        storage.all()[key].save()
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
