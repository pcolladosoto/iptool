"""
    Module Notes:
        + When returning IPs as integers we are masking them with 0xFFFFFFF
            because Python's number representation will be C2 when dealing
            with bitwise operations. As subnet masks should always begin with
            a bit set to 1, Python interpreted the BRD address as a negative
            number as it should according to the C2 scheme... What we are doing
            with the 0xFFFFFFFF mask is removing the trailing 1s so that the number
            becomes positive. We should take into account Python offers the abstraction
            of working with an "infinite" number of sign bits. As the mask will
            also be extended to the same length we are cancelling all the sign 1s
            making our number be interpreted as a negative one. In other words, we
            are "making our number "positive" by truncating the "negative" part.

            We could also add 2**32 (or 1 << 32) to the end result so that we flip
            the bit left of the 31st one, causing a carry that will change the
            magnitudes sign in the end. We nevertheless like masks more...

            Info taken from:
                https://stackoverflow.com/questions/20766813/how-to-convert-signed\
                -to-unsigned-integer-in-python#20768199
"""

def addr_to_binary(addr):
    bin_ip, loop_count = 0, 0
    for x in reversed(addr.split('/')[0].split('.')):
        bin_ip |= int(x) << loop_count * 8
        loop_count += 1
    return bin_ip & 0xFFFFFFFF

def binary_to_addr(binary):
    return ".".join(str(binary >> 8 * i & 0xFF) for i in range(3, -1, -1))

def get_net_addr(subn):
    mask = 0
    for i in range(int(subn.split('/')[1])):
        mask |= 0x1 << (31 - i)
    return (addr_to_binary(subn) & mask) & 0xFFFFFFFF

def get_brd_addr(subn):
    mask = 0
    for i in range(int(subn.split('/')[1])):
        mask |= 0x1 << (31 - i)
    return (get_net_addr(subn) | ~mask) & 0xFFFFFFFF

def get_binary(addr, ip_v = 4):
    str_addr = ""
    b_addr = addr_to_binary(addr)

    for i in range(8 * ip_v):
        str_addr = str(((1 << i) & b_addr) >> i) + str_addr

        if (i + 1) % 4 == 0:
            str_addr = ' ' + str_addr

    return str_addr.lstrip()

def get_hex(addr, ip_v = 4):
    str_addr = ""
    b_addr = addr_to_binary(addr)

    for i in range(2 * ip_v):
        str_addr = '    ' + format((b_addr >> (i * 4)) & 0xF, 'X') + str_addr

    return '0x' + str_addr[1:]
