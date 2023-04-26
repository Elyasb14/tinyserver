#!/usr/bin/env python3

# Imports
import argparse
from easysnmp import Session
import math

'''
useful OIDs
uptime = 1.3.6.1.2.1.1.3.0
cpu temp = 1.3.6.1.2.1.25.1.8
'''

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
parser.add_argument("-H", "--host", required=True, help="host to connect to")
parser.add_argument("-p", "--port", required=True, help="port to connect to")
parser.add_argument("-o", "--oid", required=True, help="SNMP OID to get the value for")
parser.add_argument("-C", "--community", default="public", help="SNMP community")
args = parser.parse_args()

HOST = args.host
PORT = args.port
SNMP_OID = args.oid
COMMUNITY = args.community

# iniating the SNMP Session
session = Session(hostname=f"{HOST}:{PORT}", community=COMMUNITY, version=2)

# isolating OID variable for value
try:
    value = session.get(SNMP_OID).value
    value = float(value)
    print(value)
except:
    print("CRITICAL: Failed to connect to device")
    exit(2)