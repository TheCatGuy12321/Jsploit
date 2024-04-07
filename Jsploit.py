from typing import Dict, TextIO
import cmd2, os

modules = {
            "exploit":{
                "test_exploit": "./modules/exploit/test_exploit.py",
                "test_exploit2": "./modules/exploit/test_exploit2.py"
            },
            "listener":{
                "test_listener": "./modules/listener/test_listener.py",
                "aaaaa_listener": "./modules/listener/aaaaa_listener.py"
            },
            "shellcode":{
                "test_shellcode": "./modules/shellcode/test_shellcode.py"
            }
        }

search_results = {}

def f_search(keyword, i_dict: dict):
    global search_results
    for i in i_dict.items():
        if type(i[1]) == dict:
            f_search(keyword, i[1])
        else:
            if keyword in i[0] or keyword in i[1]:
                search_results[i[0]] = i[1]
            

class CLI(cmd2.Cmd):
    prompt = "Jsploit >> "
    intro = """
     _                        __            __   _    
     L]     ____     _ ___    LJ    ____    LJ  FJ_   
     | L   F ___J   J '__ J   FJ   F __ J      J  _|  
     | |  | '----_  | |--| | J  L | |--| |  FJ | |-'  
.--__J J  )-____  L F L__J J J  L F L__J J J  LF |__-.
J\\_____/JJ\\______/FJ  _____/LJ__LJ\\______/FJ__L\\_____/
 J_____/  J______F |_J_____F |__| J______F |__|J_____F
                                             L_J   """

    def do_help(self, arg: str) -> bool | None:
        'Displays the help message'
        return super().do_help(arg)
    
    def do_quit(self, line):
        'Quits the program'
        print("\nBye")
        return True
    
    def do_exit(self, line):
        'Exits the program'
        print("\nBye")
        return True
    
    def do_clear(self, line):
        'Clears the screen'
        os.system("cls")
    
    def do_search(self, keyword):
        global search_results
        'Searches for modules'
        search_results = {}
        keys = []
        temp = {}
        f_search(keyword, modules)
        for k,v in search_results.items():
            keys.append(k)
        keys = sorted(keys) # sort alphabetical order
        for k in keys:
            temp[k] = search_results[k]
        search_results = temp
        i = 0
        for k,v in search_results.items():
            i += 1
            print(str(i) + ")  " + str(k), str(v))

if __name__=="__main__":
    command = CLI(completekey='tab')
    command.cmdloop()