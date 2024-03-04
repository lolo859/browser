import webbrowser
from termcolor import colored
import system.shellter_main
def execute(arg:list):
    browser=arg[0]
    if type(browser)==str:
        if system.shellter_main.connectt()==True:
            webbrowser.open(browser)
        else:
            print(colored("Vous devez connecté à internet pour utiliser ce module","red"))
    else:
        print(colored("L'URl n'est pas bonne","red",))