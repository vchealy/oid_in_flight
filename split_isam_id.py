# split_isam_id.py

import pandas as pd

from bin_to_dec import three_bit_to_decimal

def get_isam_iin_oid_sum_processes(df, isam_list):
    # Get number of processes per ISAM
    df1 = pd.DataFrame(columns=['IIN', 'OID','ISAM ID', 'Process Count'])
    for item in isam_list:
        # print(item)
        # exit()
        processes = df['iin_isam_id'].value_counts()[item]
        # print(processes)
        # exit()
        iin,oid, isamid = column_split(item)
        oid = three_bit_to_decimal(oid)  # Remark out this is you just want the Hex value in the ISAM ID (prepare_toc_dfs.py as well)
        d = {'IIN': [iin],'OID':[oid], 'ISAM ID': [isamid], 'Process Count':[processes]}
        df2 = pd.DataFrame(data=d)
        df1 = pd.concat([df1, df2])
    df = drop_columns(df1)
    return df


def column_split( item):
    iin = item[:6]
    oid = item[6:10]
    isamid = item[10:]
    return iin, oid, isamid


def drop_columns(df):
    df= df.drop(['IIN', 'ISAM ID'], axis=1)
    return df