# grph.py

'''
     Show summary as a graph
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_summary(df, filename):
     summary_graph_name = filename[:-5] + '_Summary.pdf'
     colors = ['green', 'blue', 'purple', 'brown', 'teal']
     df.plot.bar(x='OID', y='Total Processes', color = colors)

     plt.title('OID Summary')
     plt.xlabel('OID')
     plt.ylabel('Processes')
     plt.savefig(summary_graph_name, bbox_inches="tight") # Save as pdf
     # plt.show()
     # exit()
     return  summary_graph_name  

