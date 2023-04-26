#!/usr/bin/env python3

import argparse
from easysnmp import Session

'''
useful OIDs
uptime = 1.3.6.1.2.1.1.3.0
cpu temp = 1.3.6.1.2.1.25.1.8
'''

parser = argparse.ArgumentParser(
    description="makes snmp requests to host with given OID"
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
    print(value/6000)
except:
    print("CRITICAL: Failed to connect to device")
    exit(2)