from multiprocessing import Value
from re import search
from typing import Dict, TextIO
import cmd, os

modules = { # name: [path, description, target]
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

search_results = {} # variable to store search results
search_results_use = {}

def f_search(keyword, i_dict: dict): # function to search a nested dictionary
    global search_results
    for i in i_dict.items():
        if type(i[1]) == dict:
            f_search(keyword, i[1])
        else:
            if keyword in i[0] or keyword in i[1]:
                search_results[i[0]] = i[1]

def f_search_type(keyword, i_dict: dict): # function to search a nested dictionary but only search the path (used to identify the modules that are a specific type)
    global search_results
    for i in i_dict.items():
        if type(i[1]) == dict:
            f_search_type(keyword, i[1])
        else:
            if keyword in i[1]:
                search_results[i[0]] = i[1]

def f_search_use(keyword, i_dict: dict): # function to search a nested dictionary (used by use command)
    global search_results_use
    for i in i_dict.items():
        if type(i[1]) == dict:
            f_search_use(keyword, i[1])
        else:
            if keyword == i[0] or keyword == i[1]:
                search_results_use[i[0]] = i[1]
            

class CLI(cmd.Cmd):
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

    def do_help(self, arg: str) -> bool | None: # display help message
        'Displays the help message'
        return super().do_help(arg)
    
    def do_quit(self, line): # quit the program
        'Quits the program'
        print("\nBye")
        quit()
    
    def do_exit(self, line): # same as quit
        'Exits the program'
        print("\nBye")
        exit()
    
    def do_clear(self, line): # clear the screen
        'Clears the screen'
        global search_results
        os.system("cls")
        search_results = {}
    
    def do_search(self, keyword): # search modules
        'Searches for modules'
        global search_results
        search_results = {}
        keys = []
        temp = {}
        f_search(keyword, modules)
        for k,v in search_results.items(): keys.append(k)
        keys = sorted(keys) # sort alphabetical order
        for k in keys: temp[k] = search_results[k]
        search_results = temp
        print("""
  #        NAME                          PATH
  -        ----                          ----""")
        i = 0
        for k,v in search_results.items():
            i += 1
            print("  {num:<9}{name:30}{details}".format(num=i, name=k, details=v))
    
    def do_show(self, keyword: str):
        'Show or list options/modules'
        global search_results
        show_options = ["module", "modules", "exploit", "exploits", "listener", "listeners", "shellcode", "shellcodes", "options", "option"]
        if keyword.lower() not in show_options:
            print("Error: unknown option %s"%keyword)
        else:
            option = show_options.index(keyword)
            match option:
                case 0 | 1: # show modules
                    search_results = {}
                    print("""
  #        NAME                          PATH
  -        ----                          ----""")
                    temp = {}
                    keys = []
                    f_search_type("", modules)
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{details}".format(num=i, name=k, details=v))

                case 2 | 3: # show exploits
                    search_results = {}
                    print("""
  #        NAME                          PATH
  -        ----                          ----""")
                    temp = {}
                    keys = []
                    f_search_type("exploit/", modules)
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{details}".format(num=i, name=k, details=v))
                
                case 4 | 5: # show listeners
                    search_results = {}
                    print("""
  #        NAME                          PATH
  -        ----                          ----""")
                    temp = {}
                    keys = []
                    f_search_type("listener/", modules)
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{details}".format(num=i, name=k, details=v))
                
                case 6 | 7: # show shellcodes
                    search_results = {}
                    print("""
  #        NAME                          PATH
  -        ----                          ----""")
                    temp = {}
                    keys = []
                    f_search_type("shellcode/", modules)
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{details}".format(num=i, name=k, details=v))
                
                case 8 | 9: # show options to a module
                    pass
        print()
    
    # commands to use with a module
    def do_use(self, module: str | int):
        global search_results, search_results_use, modules
        search_results_use = {}
        try:
            module_int = int(module)
            if search_results == {}: return
            if module_int > len(search_results) or module_int <= 0:
                print("Error, number out of range")
                return
            search_results_use[list(search_results)[module_int-1]] = search_results[list(search_results)[module_int-1]]
            print(search_results_use)
        except (TypeError, ValueError):
            if module == "":
                print("Please specify a module to use")
                return
            f_search_use(module, modules)
            if search_results_use == {}:
                print("No module found. Try using search %s."%module)
                return
            print(search_results_use)



if __name__=="__main__":
    command = CLI(completekey='tab') # create instance
    command.cmdloop() # run