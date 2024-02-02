#!/usr/bin/env python3
"""
console.py
"""
import cmd
from models.base_model import BaseModel
import cmd
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    hbnbcommand
    """
    prompt = "(hbnb) "
    CC = { "BaseModel" }

    def do_quit(self, arg):
        """
        quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF
        """
        print()
        return True

    def emptyline(self):
        """
        empty line
        """
        pass
    
    def do_create(self, arg):
        """
        CREATE.
        """
        SP = shlex.split(arg)
        N = SP[0]
        if not (SP):
            print("** class name missing **")
        elif N not in self.CC:
            print("** class doesn't exist **")
        else:
            yues = eval(N)().id
            print(yues)
            storage.save()
    def do_show(self, arg):
        """
        Show
        """
        SP = shlex.split(arg)
        N1 = SP[0]

        if len(SP) == 0 or SP == "" or SP is None  :
            print("** class name missing **")
        elif N1 not in self.CC:
            print("** class doesn't exist **")
        elif len(SP) < 2 or len(SP) == 1:
            print("** instance id missing **")
        else:
        
            K = "{}.{}".format(N1, SP[1])
            if K in storage.all():
                print(storage.all()[K])
            else:
                print("** no instance found **")
                
    def do_destroy(self, arg):
        """destroy"""
        SP = shlex.split(arg)
        D = storage.all()
        
        if len(SP) == 0 or SP == "" or SP == None:
            print("** class name missing **")
            return
        elif len(SP) == 1 or len (SP) < 2:
            print("** instance id missing **")
            return
        elif SP[0] not in self.CC:
            print("** class doesn't exist **")
            return
        else:
        
            key = SP[0] + '.' + SP[1]
            if key in D:
                del D[key]
                storage.save()
            else:
                print("** no instance found **")
                
    def do_all(self, arg):
        """
         ALL
        """
        D = storage.all()

        SP = shlex.split(arg)
        
        N1 = SP[0]
        if N1 not in self.CC:
            print("** class doesn't exist **")

        elif len(SP) == 0:
            for key, value in D.items():
                print(str(value))
        
        else:
            
            for key, value in D.items():
                if key.split('.')[0] == N1:
                    print(str(value))
    def do_update(self, arg):
        """
    Updates
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("* class name missing *")
        elif args[0] not in self.CC:
            print("* class doesn't exist *")
        elif len(args) < 2:
            print("* instance id missing *")
        elif len(args) < 3:
            print("* attribute name missing *")
        elif len(args) < 4:
            print("* value missing *")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            atname = args[3]
            
            keyI = class_name + "." + instance_id
            dicI = storage.all()
            try:
                instanceU = dicI[keyI]
            except KeyError:
                print("** no instance found **")
                return
            try:
                typeA = type(getattr(instanceU,attribute_name))
                atname = typeA(atname)
            except AttributeError:
                pass
            setattr(instanceU, attribute_name,atname)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
