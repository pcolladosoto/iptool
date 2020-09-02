def __request_ip__(self, subnet):
    if subnet in self.next_subn_addr:
        self.next_subn_addr[subnet] += 1
        return self.__binary_to_addr__(self.next_subn_addr[subnet] - 1) + '/' + subnet.split('/')[1]
    raise ValueError("The specified subnet hasn't been created yet!")

def __addr_to_binary__(self, addr):
    bin_ip, loop_count = 0, 0
    for x in reversed(addr.split('/')[0].split('.')):
        bin_ip |= int(x) << loop_count * 8
        loop_count += 1
    return bin_ip

def __binary_to_addr__(self, bin):
    addr = ""
    for i in range(3, -1, -1):
        addr += str(bin >> 8 * i & 0xFF) + '.'
    return addr[:len(addr) - 1]

def __get_net_addr__(self, subn):
    mask = 0
    for i in range(int(subn.split('/')[1])):
        mask |= 0x1 << (31 - i)
    return self.__addr_to_binary__(subn) & mask

def __get_brd_addr__(self, subn):
    mask = 0
    for i in range(int(subn.split('/')[1])):
        mask |= 0x1 << (31 - i)
    return self.__get_net_addr__(subn) | ~mask