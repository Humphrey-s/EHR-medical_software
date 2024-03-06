#!/usr/bin/python3
"""console for EHR"""
import cmd
from model import storage
from model.base_model import BaseModel
from model.doctor import Doctor
from model.patient import Patient


classes = {"Doctor": Doctor, "Patient": Patient}

class EmhrCommand(cmd.Cmd):

    prompt= "(emhr) "

    def do_create(self, args):
        """creates user\nUsage: create <class> <name>"""

        if len(args) == 0:
            print("** No class specified **")

        args = args.split(" ")

        if len(args) < 2:
            print("** no name specified **")
        if len(args) < 3:
            print("** National id missing **")


        for key in classes.keys():
            if key == "Patient":
                instance = classes[key]()
            if key == "Doctor":
                instance = classes[key]()
        
        instance.name = args[1]
        instance.national_id = args[2]
        print(instance.id)
        storage.new(instance)
        storage.save()
        print("me")

    def do_all(self, args):
        lst = []
        obj = storage.all(classes[args])
        for key in obj.keys():
            lst.append(str(obj[key]))

        print(lst)

    def do_quit(self, args):
        """Exits the Emhr console"""
        quit()


if __name__ == "__main__":
    EmhrCommand().cmdloop()
