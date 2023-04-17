#!/usr/bin/env python3

# Imports
import argparse
from enum import IntEnum
from xmlrpc.client import boolean
from easysnmp import Session
import math

# determine whether value is acceptable or not


class Status(IntEnum):
    UNKNOWN = -1
    OK = 0
    WARNING = 1
    CRITICAL = 2

# returns the status dependent on arguments given


def value_processor(
    expect_high: bool, expect_low: bool, crit_val: float, warn_val: float, value: float
):
    '''
    Returns State of Health based off critical & warning values against SNMP request
    expect_high -- used when a low value is critical/warning e.g It's acceptable if the value is higher
    expect_low --  used when a high value is critical/warning e.g It's acceptable if the value is lower
    crit_val -- 'critical value' alert/notification level condition
    warn_val -- 'warning value' values are outside of nominal
    value --    SNMP returned value e.g 1, 'charging, etc
    '''
    if expect_high:
        if value < crit_val:
            if TIME_CONVERSION:
                print(f"CRITICAL: {time_seconds(value)} < {crit_val}")
                exit(Status.CRITICAL)
            print(f"CRITICAL: {value} < {crit_val}")
            exit(Status.CRITICAL)
        if value < warn_val:
            if TIME_CONVERSION:
                print(f"CRITICAL: {time_seconds(value)} < {crit_val}")
                exit(Status.CRITICAL)
            print(f"WARNING: {value} < {warn_val}")
            exit(Status.WARNING)
        if TIME_CONVERSION:
            print(f'OK: {time_seconds(value)}')
            exit(Status.OK)
        print(f"OK: {value}")
        exit(Status.OK)

    if expect_low:
        if value > crit_val:
            if TIME_CONVERSION:
                print(f"CRITICAL: {time_seconds(value)} < {crit_val}")
                exit(Status.CRITICAL)
            print(f"CRITICAL: {value} > {crit_val}")
            exit(Status.CRITICAL)
        if value > warn_val:
            if TIME_CONVERSION:
                print(f"CRITICAL: {time_seconds(value)} < {crit_val}")
                exit(Status.CRITICAL)
            print(f"WARNING: {value} > {warn_val}")
            exit(Status.WARNING)
        if TIME_CONVERSION:
            print(f'OK: {time_seconds(value)}')
            exit(Status.OK)
        print(f"OK: {value}")
        exit(Status.OK)


# checks if both values are entered, if so returns an error
def value_asserter(flag_1, flag_2):
    if (flag_1 and flag_2) or (not flag_1 and not flag_2):
        parser.print_help()
        exit(1)
    return True


def time_seconds(value):
    '''Returns UNIX time in human readable format'''
    value = float(value)
    hours = math.floor(value / 3600)
    days = math.floor(hours / 24)
    remainder = value - (hours * 3600)
    remainder_hours = hours - (days * 24)
    minutes = math.floor(remainder / 60)
    seconds = remainder - int(minutes * 60)
    feedback = f'Device has been online for {days} days, {remainder_hours} hours & {minutes} minutes & {seconds} seconds '
    return feedback


parser = argparse.ArgumentParser(
    description="extracts equipment status variable via EasySNMP and returns state of health dependent on arguments given"
)
parser.add_argument(
    "-H",
    "--host",
    required=True,
    help="host to connect to",
)
parser.add_argument(
    "-p",
    "--port",
    required=True,
    help="port to connect to",
)
parser.add_argument(
    "-c",
    "--critical_value",
    required=True,
    type=float,
    help="Set status to CRITICAL if value is higher",
)
parser.add_argument(
    "-w",
    "--warning_value",
    required=True,
    type=float,
    help="Set status to WARN if value is higher",
)
parser.add_argument(
    "--time_seconds",
    action='store_true',
    help='use if time returns in epoch seconds'
)
parser.add_argument(
    "--expect_high", action="store_true", help="if the expected value is high"
)
parser.add_argument(
    "--expect_low", action="store_true", help="if the expected value is low"
)
parser.add_argument("-o", "--oid", required=True,
                    help="SNMP OID to get the value for")
parser.add_argument("-C", "--community", default="public",
                    help="SNMP community")
args = parser.parse_args()

HOST = args.host
PORT = args.port
CRITICAL_VALUE = args.critical_value
WARNING_VALUE = args.warning_value
SNMP_OID = args.oid
COMMUNITY = args.community
EXPECT_HIGH = args.expect_high
EXPECT_LOW = args.expect_low
TIME_CONVERSION = args.time_seconds


# determines if incompatible values were given from args
value_asserter(EXPECT_HIGH, EXPECT_LOW)

# iniating the SNMP Session
session = Session(hostname=f"{HOST}:{PORT}", community=COMMUNITY, version=2)

# isolating OID variable for value
try:
    value = session.get(SNMP_OID).value
    value = float(value)
except:
    print("CRITICAL: Failed to connect to device")
    exit(2)

value_processor(EXPECT_HIGH, EXPECT_LOW, CRITICAL_VALUE, WARNING_VALUE, value)