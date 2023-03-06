# multipage_pdf.py
'''
     Putting make_toc_df inside the mylti_page_pdf
'''

import pandas as pd
# import modin.pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from pop import pop_off


def create_figure(isam_list, process_count_list):
     '''
           This is the figure, pdf page
     '''
     fig = plt.figure(figsize=(16,7))
     ax1 = plt.subplot(111) 
     plt.xticks(rotation=90)
     plt.xlabel(None)
     isam_id = isam_list[:len(isam_list)] # This will be ISAM number list
     process_count = process_count_list[:len(process_count_list)] # Associated Process Count list
     plot = ax1.bar(isam_id, process_count)

     for rect in plot:
        height = rect.get_height()
     #    ax1.text(rect.get_x() + rect.get_width()/2., 
     #             1.002*height,'%d' % int(height), 
     #             ha='center', va='bottom')
     ax1.set_title('Processes Pending', color='tab:gray', size=15, 
                   weight='bold')
     return fig


def multi_page_pdf(isam_oid_table, oid_list, filename):   # <<<< add in the oid, (isam column, process count column) as lists
     new_df = pd.DataFrame()
     oid_list.sort()
     print(oid_list)
     # print(filename)
     # exit()
     pdf_filename = filename[:-5] + '.pdf'
     with PdfPages(pdf_filename) as pdf:
          for oid in oid_list:
               x = str(oid)  # This is a page number
               print(x)
               new_df = isam_oid_table.loc[isam_oid_table['OID'] == oid]
               new_df = new_df.drop(['IIN', 'OID', 'ISAM ID'], axis= 1)
               new_df = new_df.sort_values(by=['Process Count'])
               # Get Total processes for this OID
               total_processes = new_df['Process Count'].sum()
               d = {'ISAM #':['Total Processes'],'Process Count': [total_processes]}
               df2 = pd.DataFrame(data=d)
               new_df = pd.concat([new_df, df2])
               isam_list = (new_df['ISAM #'].to_list())[:-1]
               # print(len(isam_list))
               process_count_list = new_df['Process Count'].to_list()[:-1]
               no_ones, process_count_list = pop_off(process_count_list)
               # print(len(isam_list) - no_ones )
               isam_list = isam_list[no_ones:]
               # exit()
               sheet_name= str(oid)
               with pd.ExcelWriter(filename, mode='a', engine='openpyxl', if_sheet_exists="replace") as writer:
                    new_df.to_excel(writer, sheet_name= sheet_name, index=False)
        
               # Graphics
               # Page for pdf
               create_figure(isam_list, process_count_list)
               page_number = 'OID ' + x
               plt.suptitle(page_number, color='tab:blue', size=20, weight='bold')
               plt.tight_layout(pad=5, w_pad=2)
               pdf.savefig(
                    pad_inches=0.01, 
                    transparent=True, 
                    dpi=300, 
                    orientation='landscape'
                    )
                    # plt.show()
               plt.close()
     return filename, pdf_filename