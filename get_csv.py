# get_csv.py

import glob
import pandas as pd

from os.path import getctime


def get_latest_file():

    latest_file = max(glob.glob(r'reportsIn\*csv'), key=getctime)
    new_filename = latest_file[10:-4] # Name of the file added to the folder
    df = pd.read_csv(latest_file)
    return df, new_filename