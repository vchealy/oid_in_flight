# main.py
'''
    Building a list of ISAM with a number of Processes Outstanding
'''
import pandas as pd
# import modin.pandas as pd

from os import system
from time import  strftime 

from get_csv import get_latest_file
from sort_df import df_sortby
from make_isam_list import get_isam_list
from split_isam_id import get_isam_iin_oid_sum_processes
from build_oid_summary_df import get_df_summary
from prepare_toc_dfs import build_table
from create_toc_df import make_toc_df
from move_output_file import move_it
from summary_graph import plot_summary

# Turn this off to stop pdf creation
# Also swap over the filename to line 62 rather than 63
from multipage_pdf import multi_page_pdf



def main_function():
    system('cls')
    # Build the DataFrames
    df, new_file_name = get_latest_file()
    # print(df.head)
    # exit()
    print(f'Got the file: {new_file_name}')
    filename = strftime("%Y_%m_%d-%H_%M_%S")  + '_' + new_file_name + '_Process_By_OID.xlsx'
    df_sorted = df_sortby(df)
    # df_sorted.to_excel('out_df_sorted.xlsx')
    # print(df_sorted.head)
    # exit()
    isam_list, df_isam_logical_list = get_isam_list(df_sorted)
    # print(isam_list)
    # print(df_isam_logical_list.head)
    # exit()
    print('Reordered the data')
    print(f'Got a list of all ISAM on:  {new_file_name}')
    isam_iin_oid_sum_processes = get_isam_iin_oid_sum_processes(df_sorted, isam_list)
    # print(isam_iin_oid_sum_processes)
    # exit()
    isam_oid_table, oid_list = build_table(df_sorted, isam_list)
    # print(isam_oid_table)
    # exit()
    print(f'Have the total processes by ISAM from: {new_file_name}')
    summary_worksheet_df = get_df_summary(isam_iin_oid_sum_processes, oid_list)
    summary_worksheet_df = summary_worksheet_df.sort_values(by=['OID'])
    # print(summary_worksheet_df.head)
    # exit()
    print(f'Got the total processes by OID from: {new_file_name}')

    # Create the Report
    print('Creating Summary worksheet')
    sheet_name= 'OID Summary'
    summary_worksheet_df.to_excel(filename, sheet_name= sheet_name, engine='xlsxwriter', index=False)
    # exit()
    summary_graph_name = plot_summary(summary_worksheet_df, filename)
    print('Working on OID Sheets')
    # filename = make_toc_df(isam_oid_table, oid_list, filename)
    filename, pdf_filename = multi_page_pdf(isam_oid_table, oid_list, filename)
    print('Move output to reportsOut')
    move_it(filename)
    move_it(pdf_filename)
    move_it(summary_graph_name)
    print('Task Complete')
    return

if __name__ =='__main__':
    main_function()