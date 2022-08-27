#!/usr/bin/env python3

"""Get 6to4 address from IPv4 address."""

import argparse
import sentry_sdk


def parse_args():  # pragma: no cover
    """Get arguments from CLI."""
    parser = argparse.ArgumentParser(description="Get 6to4 address from IPv4 address.")
    parser.add_argument(
        "-a",
        "--address",
        dest="address",
        action="store",
        help="IPv4 address",
        required=True,
    )
    return parser.parse_args()


def ipv4_to_ipv6(ipv4):
    """COnvert IPv4 address to IPv6."""
    ipv4_hex = ""
    ipv6_hextets = ["", ""]

    # Split input to octets
    ipv4 = ipv4.split(".", 4)

    # Convert IPv4 address to hex string
    for octet in ipv4:
        if len(hex(int(octet))[2:]) > 1:
            ipv4_hex += hex(int(octet))[2:]
        else:
            ipv4_hex += "0"
            ipv4_hex += hex(int(octet))[2:]

    # Split into hextets
    for i in range(4):
        ipv6_hextets[0] += ipv4_hex[i]
    for i in range(4, 8):
        ipv6_hextets[1] += ipv4_hex[i]

    # Convert to dec and back to remove leading zeros
    ipv6_hextets[0] = hex(int(ipv6_hextets[0], 16))[2:]
    ipv6_hextets[1] = hex(int(ipv6_hextets[1], 16))[2:]

    # Form 6to4 address
    output_6to4 = f"2002:{ipv6_hextets[0]}:{ipv6_hextets[1]}::/128"
    return output_6to4


def main():  # pragma: no cover
    """Main function."""

    sentry_sdk.init("https://14fab091f12c45d299569dcefd1bd716@app.glitchtip.com/1704")

    ipv4 = parse_args().address
    output = ipv4_to_ipv6(ipv4)
    print(output)


if __name__ == "__main__":
    main()  # pragma: no cover
