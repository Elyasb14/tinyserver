
class Device:
    def __init__(self):
        pass

    def ping(self, ip: str) -> None:
        try:
            ping_node = ping(ip)
            if ping_node.success():
                print("can ping server")
                print(f"Average rrt: {ping_node.rtt_avg_ms}")
            else:
                print("cant ping server")
        except OSError as e:
            print(e)
            print("cant ping server")
        