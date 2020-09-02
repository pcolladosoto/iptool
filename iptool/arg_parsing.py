import argparse

def parse_args(version):
    parser = argparse.ArgumentParser(description = "iptool v{}".format(version))
    parser.add_argument('ip', metavar = 'ip', type = check_valid_ip, nargs = 1, help = "IP address to work on")
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
