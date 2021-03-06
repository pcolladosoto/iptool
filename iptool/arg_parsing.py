import argparse, sys

def p_args(version):
    parser = argparse.ArgumentParser(description = "iptool v{}".format(version))
    parser.add_argument('ip', nargs = '?', help = "IP address to work on.")
    parser.add_argument('-c', '--cidr', type = check_valid_cidr, help = "Find the limits of the provided CIDR block"\
                                                                        " or whether the provided IP belongs to the CIDR block.")
    parser.add_argument('-b', '--binary', action = 'store_true', help = "Display the given IP as a BINARY number.")
    parser.add_argument('-x', '--hex', action = 'store_true', help = "Display the given IP as a HEX number.")

    parsed_args = vars(parser.parse_args())

    # print(parsed_args)

    if len(sys.argv) == 1:
        parser.print_help()
        exit(-1)
    elif len(sys.argv) == 2:
        parsed_args['binary'] = True
    else:
        if not parsed_args['ip']:
            if parsed_args['binary'] or parsed_args['hex']:
                parser.error("Missing an IP!")
        else:
            check_valid_ip(parsed_args['ip'], parser)

        if (parsed_args['binary'] or parsed_args['hex']) and parsed_args['cidr']:
            parser.error("Options -c and -b or -h are incompatible!")

    return parsed_args

def check_valid_ip(ip, prsr = None):
    ip_chunks = ip.split('.')

    if len(ip_chunks) != 4:
        prsr.error("An IPv4 address MUST have exactly 4 fields")

    for x in ip_chunks:
        try:
            ix = int(x)
        except ValueError:
            prsr.error("{} is NOT an integer".format(x))
        if ix < 0 or ix > 255:
            prsr.error("{} is not a valid Byte value".format(x))

    return ip

def check_valid_cidr(cidr):
    cidr_chunks = cidr.split('/')

    if len(cidr_chunks) != 2:
        raise argparse.ArgumentTypeError("Incorrect CIDR format")

    ip = cidr_chunks[0]

    try:
        subn_mask = int(cidr_chunks[1])
    except ValueError:
        raise argparse.ArgumentTypeError("{} is NOT a valid subnet mask value".format(cidr_chunks[1]))

    check_valid_ip(ip)

    if subn_mask < 0 or subn_mask > 32:
        raise argparse.ArgumentTypeError("{} is NOT a valid subnet mask".format(subn_mask))

    return cidr
