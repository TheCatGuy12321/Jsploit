import cmd2, os

class CLI(cmd2.Cmd):
    prompt = "Jsploit >> "
    intro = """
     _              _                                   __            __   _    
     L]    ____    FJ_      ___ _     ____     _ ___    LJ    ____    LJ  FJ_   
     | L  F __ J  J  _|    F __` L   F ___J   J '__ J   FJ   F __ J      J  _|  
     | | | _____J | |-'   | |--| |  | '----_  | |--| | J  L | |--| |  FJ | |-'  
.--__J J F L___--.F |__-. F L__J J  )-____  L F L__J J J  L F L__J J J  LF |__-.
J\\_____/J\\______/F\\_____/J\\____,__LJ\\______/FJ  _____/LJ__LJ\\______/FJ__L\\_____/
 J_____/ J______F J_____F J____,__F J______F |_J_____F |__| J______F |__|J_____F
                                             L_J                                """
    
    def do_help(self, arg: str) -> bool | None:
        'Displays the help message'
        return super().do_help(arg)
    
    def do_quit(self, line):
        'Quits the program'
        print("\nBye")
        return True
    
    def do_clear(self, line):
        'Clears the screen'
        os.system("cls")

if __name__=="__main__":
    command = CLI(completekey='tab')
    command.cmdloop()