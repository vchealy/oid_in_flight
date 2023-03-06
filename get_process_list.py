# get_process_list.py
'''
    Create a list of processes for each ISAM
'''


def get_isam_processes(df, isam):
    proclist = []
    df = df[df.iin_isam_id == isam]
    proclist = str(df['process_id'].tolist())[1:-1] # Convert to string and remove outer square brackets

    return proclist