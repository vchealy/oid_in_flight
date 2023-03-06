# v
'''
    This module is to build a dataframe that will be the summary worksheet of the report
    Take the 
'''
import pandas as pd
# import modin.pandas as pd

def get_df_summary(df, oid_list):
    # Get a list of oids
    summary_df = pd.DataFrame(columns=['OID', '# of ISAM', 'Total Processes'])
    for oid in oid_list:
        df_oid = df[df['OID']==oid] #Gets all the rows for the OID 
        isam_with_oid = len(df_oid.index) # Count number of ISAM in the OID
        sumup = df_oid['Process Count'].sum()
        d = {'OID':[oid], '# of ISAM':[isam_with_oid],'Total Processes': [sumup]}
        df2 = pd.DataFrame(data=d)
        summary_df = pd.concat([summary_df, df2]) 
    # exit()
    return summary_df