from .arg_parsing import p_args
from .ip_handling import get_net_addr, get_brd_addr, binary_to_addr, addr_to_binary, get_binary, get_hex

def main(version):
    args = p_args(version)

    if args['cidr'] != None:
        cidr_blk = args['cidr']

        b_net_addr = get_net_addr(cidr_blk)
        b_brd_addr = get_brd_addr(cidr_blk)

        if args['ip'] == None:
            n_ips = b_brd_addr - b_net_addr + 1

            # We could have also computed the available number of addresses as:
            # n_ips = 2**(32 - int(cidr_blk.split('/')[1]))

            net_addr = binary_to_addr(b_net_addr)
            brd_addr = binary_to_addr(b_brd_addr)

            print(  "Network (NET) address:\t\t{}\n" \
                    "Broadcast (BRD) Address:\t{}\n" \
                    "Network Range:\t\t\t{} <--> {}\n" \
                    "Number of IP addresses:\t\t{} (Including the NET and BRD addresses)".format(
                        net_addr,
                        brd_addr,
                        net_addr,
                        brd_addr,
                        n_ips
                    ))
            return

        else:
            b_ip = addr_to_binary(args['ip'])

            print("Address {} {} to the {} CIDR block.".format(args['ip'],
                                                                "BELONGS" if b_net_addr <= b_ip <= b_brd_addr else "DOESN'T BELONG",
                                                                cidr_blk))

    elif args['binary'] or args['hex']:
        if args['binary']:
            print("BINARY representation -->\t{}".format(get_binary(args['ip'])))
        if args['hex']:
            print("HEX representation -->\t\t\b\b{}".format(get_hex(args['ip'])))

        return



if __name__ == '__main__':
    main("dbg")