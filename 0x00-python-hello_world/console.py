#!/usr/bin/env python3
"""
console.py
"""
import re
import cmd
from models.base_model import BaseModel
import shlex
from models import storage
from models.user import User
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
import sys
import json


class HBNBCommand(cmd.Cmd):
    """
    hbnbcommand
    """

    completekey = 'tab' 
    prompt = "(hbnb) "
    CC = ["BaseModel", "User", "Amenity", "Place", "Review", "State", "City"]

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

        if len(SP) == 0 or SP == "" or SP is None:
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

        if len(SP) == 0 or SP == "" or SP is None:
            print("** class name missing **")
            return
        elif len(SP) == 1 or len(SP) < 2:
            print("** instance id missing **")
            return
        elif SP[0] not in self.CC:
            print("** class doesn't exist **")
            return
        else:
            key = SP[0] + "." + SP[1]
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
                if key.split(".")[0] == N1:
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
                typeA = type(getattr(instanceU, attribute_name))
                atname = typeA(atname)
            except AttributeError:
                pass
            setattr(instanceU, attribute_name, atname)
            storage.save()
    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
       
        arg_list = arg.split('.')

        cls_nm = arg_list[0]

        command = arg_list[1].split('(')

        cmd_met = command[0]

        e_arg = command[1].split(')')[0]

        al = e_arg.split(',')

        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = re.search(r"\.", arg)
        if bool(match):
            start, end = match.span()
            argl = [arg[:start], arg[end:]]

            match = re.search(r"\((.*?)\)", argl[1])
            if bool(match):
                start, end = match.span()
                command_text = argl[1][:start]
                command_argument = match.group()[1:-1]
                command = [command_text, command_argument]

                if cmd_met in argdict.keys():
                    if cmd_met != "update":
                        call = f"{argl[0]} {e_arg}"
                        return argdict[cmd_met](call)
                    else:
                        ob = al[0]
                        ana = al[1:]
                        print (ana)
                        if isinstance(ana, dict):
                            for k, v in dic.items():
                                return argdict[cmd_met]("{} {} {} {}".format(cls_nm, ob, k, v))
                        else:
                             return argdict[cmd_met]("{} {} {} {}".format(cls_nm, ob, al[1], al[2]))

        print(f"*** Unknown syntax: {arg}")

        return False
    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = shlex.split(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count) 

if __name__ == "__main__":
    HBNBCommand().cmdloop()
