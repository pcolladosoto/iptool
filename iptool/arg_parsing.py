import argparse

def parse_args(version):
    parser = argparse.ArgumentParser(description = "iptool v{}".format(version))
    parser.add_argument('ip', type = check_valid_ip, nargs = '?', help = "IP address to work on")
    parser.add_argument('-l', '--limits', type = check_valid_cidr, help = "Find the limits of the provided CIDR block")
    parser.add_argument('-b', '--binary', help = "Enable displaying the IP addresses as binary numbers")
    return vars(parser.parse_args())

def check_valid_ip(ip):
    ip_chunks = ip.split('.')

    if len(ip_chunks) != 4:
        raise argparse.ArgumentTypeError("An IPv4 address MUST have exactly 4 fields")

    for x in ip_chunks:
        try:
            ix = int(x)
        except ValueError:
            raise argparse.ArgumentTypeError("{} is NOT an integer".format(x))
        if ix < 0 or ix > 255:
            raise argparse.ArgumentTypeError("{} is not a valid Byte value".format(x))

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
