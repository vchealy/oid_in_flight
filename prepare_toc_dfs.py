# prepare_toc_dfs.py
'''
     This is to create each of the TOC dataframes.
     Each dataframe will be a worksheet in the final output
     Import the df_sorted
     The first 10 characters of the ISAM ID will determine which TOC- 10Blip
     Create a df using the last four characters of the 10Blip - 4Blip
     Use the 4Blip as the sheet name 


     Split the column ISAM ID into thee columns but keep the original column
    
'''

import pandas as pd
# import modin.pandas as pd

from bin_to_dec import three_bit_to_decimal
from get_process_list import get_isam_processes

def build_table(df, isam_list):
    # Get number of processes per ISAM
    df1 = pd.DataFrame(columns=['ISAM #', 'Logical Group', 'IIN', 'OID','ISAM ID','Process Count', 'Process List'])
    df_dropped_duplicates = df.drop_duplicates(subset=['iin_isam_id'])
    # df_dropped_duplicates.to_excel('df_dropped_duplicates.xlsx')
    # exit()
    for item in isam_list:
        proclist = get_isam_processes(df, item)
        get_group = (df_dropped_duplicates.loc[df_dropped_duplicates['iin_isam_id'] == item, 'logical_group'])
        get_group = get_group.to_frame()
        get_group = (str((list(get_group.values))[0]))[2:-2]

        processes = df['iin_isam_id'].value_counts()[item] # Count the number of processes per ISAM
        iin,oid, isamid = column_split(item)
        oid = three_bit_to_decimal(oid)   # Remark out this is you just want the Hex value in the ISAM ID (split_isam_id.py as well)
        d = {
            'ISAM #': [item], 
            'Logical Group':[get_group], 
            'IIN': [iin],'OID':[oid], 
            'ISAM ID': [isamid], 
            'Process Count': [processes], 
            'Process List': [proclist]
            }
        df2 = pd.DataFrame(data=d)
        df1 = pd.concat([df1, df2]) 
    oid_list = get_oid_list(df1)
    # exit()
    return df1, oid_list


def column_split( item):
    iin = item[:6]
    oid = item[6:10]
    isamid = item[10:]
    return iin, oid, isamid


def get_oid_list(df1):
     oid_list = list(set(df1['OID'].to_list()))
     return oid_list


# def create_toc_df():
