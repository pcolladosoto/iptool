from iptool import arg_parsing, ip_handling

V_NUMBER = "0.0.1"

def main():
    args = arg_parsing.parse_args(V_NUMBER)
    # print(args)

if __name__ == '__main__':
    main()