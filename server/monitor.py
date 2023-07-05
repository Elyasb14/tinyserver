from pythonping import ping

class Monitor:
    def __init__(self, ip: str) -> None:
        self.ip = ip

    def ping_ip(self) -> str:
        '''
        pings given ip and logs in logs/ping_log.txt
        '''
        try:
            ping_node = ping(self.ip)
            if ping_node.success():
                return f"can ping {self.ip}"
            else:
                return f"can't ping {self.ip}"
        except OSError as e:
            return f"cant ping {self.ip}. Error: {e}"
    
    def snmp_ip(self, oid: str) -> str:
        '''
        returns given oid value from snmp request
        '''
        from easysnmp import Session
        session = Session(hostname=f"{self.ip}:161", community='public', version=2)
        if oid == '1.3.6.1.2.1.25.1.8':
            value = f'{float(session.get(oid).value) / 1000} deg C'
        elif oid == '1.3.6.1.2.1.1.3.0':
            value = f"{(float(session.get(oid).value) / 100) / 60} minutes"
        else:
            value = session.get(oid).value
        return value



if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('server/nodes.csv')
    oids = {'sys info': '1.3.6.1.2.1.1.1.0',
            'cpu temp, deg c': '1.3.6.1.2.1.25.1.8',
            'uptime': '1.3.6.1.2.1.1.3.0'
            }
    for ip in df['ip']:
        server = Monitor(ip)
        for oid in oids.values():
            print(server.snmp_ip(oid))
        with open("/Users/ebianchi/programs/tinyserver/server/logs/ping_log.txt", 'a') as file:
            file.write(f'{server.ping_ip()} \n')