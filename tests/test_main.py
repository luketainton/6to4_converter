#!/usr/bin/env python3

"""Test cases for main.py."""

from app.main import ipv4_to_ipv6


def test_ipv4_to_ipv6():
    """Test case for ipv4_to_ipv6()."""
    result = ipv4_to_ipv6("192.168.0.1")
    assert result == "2002:c0a8:1::/128"
