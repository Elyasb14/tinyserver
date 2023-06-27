from paramiko import SSHClient, AutoAddPolicy

def sftp_ip(ip: str) -> None:
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(hostname=ip,username='ebianchi',password='Galoisgroup#2')
        ftp_client = ssh_client.open_sftp()
        ftp_client.chdir('/Users/ebianchi/programs/tinyweb/tinyweather/data/')
        data_dir = ftp_client.listdir()
        for file in data_dir:
            if file == ".config":
                continue
            print(file)
            ftp_client.get(remotepath=f'/Users/ebianchi/programs/tinyweb/tinyweather/data/{file}', localpath=f'/Users/ebianchi/programs/tinyserver/data/{file}')
        ftp_client.close()
        return f"data retrieval successful from {ip}"


if __name__ == "__main__":
    pass

