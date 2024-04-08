import cmd, os

class mod_option():
    def __init__(self, name: str, description: str, optional: bool):
        self.name = name
        self.desc = description
        self.opt = optional

    def __str__(self) -> str:
        return (f"{self.name:<30}{self.desc:<50}  (required: {self.opt})")

modules = { # name: [path, description, options]
            "exploit":{
                "test_exploit": ["./modules/exploit/test_exploit.py", "test", [mod_option("RHOST", "test", True)]],
                "test_exploit2": ["./modules/exploit/test_exploit2.py", "test", [mod_option("RHOST", "test", True)]]
            },
            "listener":{
                "test_listener": ["./modules/exploit/test_listener.py", "test", [mod_option("RHOST", "test", True)]],
                "aaaaa_listener": ["./modules/exploit/aaaaa_listener.py", "test", [mod_option("RHOST", "test", True)]]
            },
            "shellcode":{
                "test_shellcode": ["./modules/exploit/test_shellcode.py", "test", [mod_option("RHOST", "test", True)]]
            }
        }

search_results = {} # variable to store search results
current_module = {}

def f_search(keyword, i_dict: dict): # function to search a nested dictionary
    global search_results
    for i in i_dict.items():
        if type(i[1]) == dict:
            f_search(keyword, i[1])
        else:
            if keyword in i[0] or keyword in i[1][0] or keyword in i[1][1]:
                search_results[i[0]] = i[1]

def f_search_use(keyword, i_dict: dict): # function to search a nested dictionary (used by use command)
    global current_module
    for i in i_dict.items():
        if type(i[1]) == dict:
            f_search_use(keyword, i[1])
        else:
            if keyword in i[0] or keyword in i[1][0] or keyword in i[1][1]:
                current_module[i[0]] = i[1]

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

    def do_banner(self, line):
        'Prints the banner'
        print("""
     _                        __            __   _    
     L]     ____     _ ___    LJ    ____    LJ  FJ_   
     | L   F ___J   J '__ J   FJ   F __ J      J  _|  
     | |  | '----_  | |--| | J  L | |--| |  FJ | |-'  
.--__J J  )-____  L F L__J J J  L F L__J J J  LF |__-.
J\\_____/JJ\\______/FJ  _____/LJ__LJ\\______/FJ__L\\_____/
 J_____/  J______F |_J_____F |__| J______F |__|J_____F
                                             L_J   """)

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
        if search_results == {}:
            print("No results found.")
            return
        for k,v in search_results.items(): keys.append(k)
        keys = sorted(keys) # sort alphabetical order
        for k in keys: temp[k] = search_results[k]
        search_results = temp
        print("""
  #        NAME                          PATH                                                    DESCRIPTION
  -        ----                          ----                                                    -----------""")
        i = 0
        for k,v in search_results.items():
            i += 1
            print("  {num:<9}{name:30}{path:56}{desc}".format(num=i, name=k, path=v[0], desc=v[1]))
    
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
  #        NAME                          PATH                                                    DESCRIPTION
  -        ----                          ----                                                    -----------""")
                    temp = {}
                    keys = []
                    f_search("", modules)
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{path:56}{desc}".format(num=i, name=k, path=v[0], desc=v[1]))

                case 2 | 3: # show exploits
                    search_results = {}
                    print("""
  #        NAME                          PATH                                                    DESCRIPTION
  -        ----                          ----                                                    -----------""")
                    temp = {}
                    keys = []
                    f_search("", modules["exploit"])
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{path:56}{desc}".format(num=i, name=k, path=v[0], desc=v[1]))
                
                case 4 | 5: # show listeners
                    search_results = {}
                    print("""
  #        NAME                          PATH                                                    DESCRIPTION
  -        ----                          ----                                                    -----------""")
                    temp = {}
                    keys = []
                    f_search("", modules["listener"])
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{path:56}{desc}".format(num=i, name=k, path=v[0], desc=v[1]))
                
                case 6 | 7: # show shellcodes
                    search_results = {}
                    print("""
  #        NAME                          PATH                                                    DESCRIPTION
  -        ----                          ----                                                    -----------""")
                    temp = {}
                    keys = []
                    f_search("", modules["shellcode"])
                    for k,v in search_results.items():
                        keys.append(k)
                    keys = sorted(keys) # sort alphabetical order
                    for k in keys:
                        temp[k] = search_results[k]
                    search_results = temp
                    i = 0
                    for k,v in search_results.items():
                        i += 1
                        print("  {num:<9}{name:30}{path:56}{desc}".format(num=i, name=k, path=v[0], desc=v[1]))
                
                case 8 | 9: # show options
                    if current_module == {}:
                        print("No module selected")
                        return
                    for i in range(len(current_module[list(current_module)[0]][2])):
                        print("""
#         NAME                          DESCRIPTION                                         OPTIONAL
-         ----                          -----------                                         --------""")
                        print(f"{str(i+1):10}{current_module[list(current_module)[0]][2][i]}")

        print()
    
    # commands to use with a module
    def do_use(self, module: str | int):
        'Select a module'
        global search_results, current_module, modules
        current_module = {}
        try:
            module_int = int(module)
            if search_results == {}: return
            if module_int > len(search_results) or module_int <= 0:
                print("Error, number out of range")
                return
            current_module[list(search_results)[module_int-1]] = search_results[list(search_results)[module_int-1]]
        except (TypeError, ValueError):
            if module == "":
                print("Please specify a module to use")
                return
            f_search_use(module, modules)
            if current_module == {}:
                print("No module found. Try using search %s."%module)
                return
        return

if __name__=="__main__":
    command = CLI(completekey='tab') # create instance
    command.cmdloop() # run