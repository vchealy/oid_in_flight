# move_output_file.py

import shutil


def move_it(filename):
    destination = 'reportsOut'
    shutil.move(filename, destination)
    return
