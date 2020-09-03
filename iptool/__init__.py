import arg_parsing, ip_handling

V_NUMBER = "0.0.1"

def main():
    args = arg_parsing.parse_args(V_NUMBER)

    # print(args)

    if args['limits'] != None:
        cidr_blk = args['limits']

        b_net_addr = ip_handling.get_net_addr(cidr_blk)
        b_brd_addr = ip_handling.get_brd_addr(cidr_blk)

        n_ips = b_brd_addr - b_net_addr + 1

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


if __name__ == '__main__':
    main()