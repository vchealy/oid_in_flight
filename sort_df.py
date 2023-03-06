# sort_df.py

def df_sortby(df):
    #  Sorting the Raw data
    df_sorted = df.sort_values(by=['iin_isam_id','process_id'])
    return df_sorted