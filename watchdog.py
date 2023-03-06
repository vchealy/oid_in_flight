# watchdog.py
'''
 Watches for .csv files being added to a folder
    Drop files into the reports folder
'''


from time import sleep 
from os.path import getctime
from os import system, listdir

from main import main_function


def watchdog():
    system('cls')
    print('OID Process Counter\nWatchdog active')
    path_to_watch = "reportsIn"
    before = dict ([(f, None) for f in listdir (path_to_watch)])
    while 1:
        sleep (1)
        after = dict ([(f, None) for f in listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: print(f'Added:  {added}')
        sleep(2)
        if added: main_function()
        if removed: print(f'Removed: {removed}')
        sleep(2)
        system('cls')
        print('OID Process Counter\nWatchdog active')
        before = after


if __name__ == '__main__':
    watchdog()