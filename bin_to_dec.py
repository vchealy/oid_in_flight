# bin_to_dec.py
'''
 Convert ISAM_OID to Bin
 Convert Bin to 3BitRight
 Convert 3BitRight to Decimal
'''

def three_bit_to_decimal(hex_id):
    binary_value = "{0:08b}".format(int(hex_id, 16))
    bit_shift_binary = binary_value[:-3]
    decimal = int(bit_shift_binary, 2)
    return decimal