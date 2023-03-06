# pop.py
'''
    Removing the ISAM with only one Pending process from the graphs
'''

def pop_off(with_ones):
    # print(with_ones)
    with_len = (len(with_ones))
    x = list(filter((1).__ne__, with_ones))
    
    without_len = len(x)
    no_ones = with_len - without_len
    # print(no_ones)

    return no_ones, x