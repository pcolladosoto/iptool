import arg_parsing, ip_handling

V_NUMBER = "0.0.1"

def main():
    args = arg_parsing.p_args(V_NUMBER)

    if args['cidr'] != None:
        cidr_blk = args['cidr']

        b_net_addr = ip_handling.get_net_addr(cidr_blk)
        b_brd_addr = ip_handling.get_brd_addr(cidr_blk)

        if args['ip'] == None:
            n_ips = b_brd_addr - b_net_addr + 1

            # We could have also computed the available number of addresses as:
            # n_ips = 2**(32 - int(cidr_blk.split('/')[1]))

            net_addr = ip_handling.binary_to_addr(b_net_addr)
            brd_addr = ip_handling.binary_to_addr(b_brd_addr)

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
            b_ip = ip_handling.addr_to_binary(args['ip'])

            print("Address {} {} to the {} CIDR block.".format(args['ip'],
                                                                "BELONGS" if b_net_addr <= b_ip <= b_brd_addr else "DOESN'T BELONG",
                                                                cidr_blk))

    elif args['binary'] or args['hex']:
        if args['binary']:
            print("BINARY representation -->\t{}".format(ip_handling.get_binary(args['ip'])))
        if args['hex']:
            print("HEX representation -->\t\t\b\b{}".format(ip_handling.get_hex(args['ip'])))

        return



if __name__ == '__main__':
    main()