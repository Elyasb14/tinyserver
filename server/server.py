from pythonping import ping


class Server:
    def __init__(self, ip: str) -> str:
        self.ip = ip

    def ping_ip(self):
        try:
            ping_node = ping(self.ip)
            if ping_node.success():
                return f"can ping {self.ip}"
            else:
                return f"can't ping {self.ip}"
        except OSError as e:
            return f"cant ping {self.ip}. Error: {e}"

    # def sftp_ip(self):
    #     with pysftp.Connection(host=f'self.ip', username="ebianchi", password="Galoisgroup#2") as connection:
    #         with connection.cd('/Users/ebianchi/programs/tinyweb/tinyweather/data'):
    #             data_dir = connection.listdir()
    #             for file in data_dir:
    #                 connection.get(f'{file}', localpath=f'data/{file}')


if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('server/nodes.csv')
    
    for ip in df['ip']:
        server = Server(ip)
        with open("/Users/ebianchi/programs/tinyserver/server/logs/ping_log.txt", 'a') as file:
            file.write(f'{server.ping_ip()} \n')