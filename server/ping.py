from pythonping import ping
import pandas as pd

# print(type(ping("192.168.86.1", verbose=True)))
df = pd.read_csv("server/nodes.csv")

for ip in df["ip"]:
    try:
        ping_node = ping(ip)
        if ping_node.success():
            print("can ping server")
            print(f"Average rrt: {ping_node.rtt_avg_ms}")
        else:
            print("cant ping server")
            print(f"Packets lost: {ping_node.stats_packets_lost}")
    except OSError as e:
        print(e)
        print("cant ping server")
        print(f"Packets lost: {ping_node.stats_packets_lost}")