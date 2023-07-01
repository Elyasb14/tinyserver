from pythonping import ping
# from paramiko import SSHClient, AutoAddPolicy

class Monitor:
    def __init__(self, ip: str) -> None:
        self.ip = ip

    def ping_ip(self) -> str:
        try:
            ping_node = ping(self.ip)
            if ping_node.success():
                return f"can ping {self.ip}"
            else:
                return f"can't ping {self.ip}"
        except OSError as e:
            return f"cant ping {self.ip}. Error: {e}"


if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('server/nodes.csv')
    for ip in df['ip']:
        server = Monitor(ip)
        with open("/Users/ebianchi/programs/tinyserver/server/logs/ping_log.txt", 'a') as file:
            file.write(f'{server.ping_ip()} \n')