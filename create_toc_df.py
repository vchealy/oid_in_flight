# create_toc_df.py
'''
     This is the code to create a single list of ISAM ID for a single OID
'''

import pandas as pd
# import modin.pandas as pd

from matplotlib.backends.backend_pdf import PdfPages as matpdf


def make_toc_df(isam_oid_table, oid_list, filename):
    # print(isam_oid_table['Logical Group'])
    # isam_oid_table.to_excel('output.xlsx')
    # # # print(oid_list)
    # exit()
    new_df = pd.DataFrame()
    oid_list.sort()
    figs = []
    for oid in oid_list:
        # print(oid)
        new_df = isam_oid_table.loc[isam_oid_table['OID'] == oid]
        new_df = new_df.drop(['IIN', 'OID', 'ISAM ID'], axis= 1)
        new_df = new_df.sort_values(by=['Process Count'])
        # Get Total processes for this OID
        total_processes = new_df['Process Count'].sum()
        d = {'ISAM #':['Total Processes'],'Process Count': [total_processes]}
        df2 = pd.DataFrame(data=d)
        new_df = pd.concat([new_df, df2])
        # print(new_df.head)
        # exit()
        sheet_name= str(oid)
        with pd.ExcelWriter(filename, mode='a', engine='openpyxl', if_sheet_exists="replace") as writer:
            new_df.to_excel(writer, sheet_name= sheet_name, index=False)
        
    return filename