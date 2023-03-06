# make_isam_list.py


def get_isam_list(df):
    # Make an ISAM list from the DataFrame
    df1 = df.iloc[:, :2]
    df2 = df.iloc[:, :2]
    # print(df)
    # exit()
    df_isam_list = df1.drop_duplicates(subset=['iin_isam_id'])
    isam_as_list = df_isam_list['iin_isam_id'].tolist()
    # print(df_isam_list.head)
    # exit()
    df_isam_logical_list = df2.drop_duplicates(subset=['iin_isam_id', 'logical_group'])
    # print(df_isam_logical_list.head)
    # exit()

    return isam_as_list, df_isam_logical_list
