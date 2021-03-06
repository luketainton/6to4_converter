#!/usr/bin/env python3

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Get 6to4 address from IPv4 address.')
    parser.add_argument('-a', '--address', dest='address', action='store', help='IPv4 address', required=True)
    args = parser.parse_args()
    return args


def get_address():
    args = parse_args()
    return args.address


def ipv4_to_ipv6(ipv4):
    ipv4Hex = ''
    ipv6Hextet1 = '2002'
    ipv6Hextet2 = ''
    ipv6Hextet3 = ''

    # Split input to octets
    ipv4 = ipv4.split('.',4)

    # Convert IPv4 address to hex string
    for octet in ipv4:
        if len(hex(int(octet))[2:])>1:
            ipv4Hex += hex(int(octet))[2:]
        else:
            ipv4Hex += '0'
            ipv4Hex += hex(int(octet))[2:]

    # Split into hextets
    for i in range(4):
        ipv6Hextet2 += (ipv4Hex[i])
    for i in range(4,8):
        ipv6Hextet3 += (ipv4Hex[i])

    # Convert to dec and back to remove leading zeros
    ipv6Hextet2 = hex(int(ipv6Hextet2,16))[2:]
    ipv6Hextet3 = hex(int(ipv6Hextet3,16))[2:]

    # Form 6to4 address
    output_6to4 = f"{ipv6Hextet1}:{ipv6Hextet2}:{ipv6Hextet3}::/128"
    return output_6to4


def main():
    ipv4 = get_address()
    output = ipv4_to_ipv6(ipv4)
    print(output)


if __name__ == '__main__':
    main()
