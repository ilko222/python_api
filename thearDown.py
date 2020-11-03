from paramiko import SSHClient
# from scp import SCPClient
from datetime import datetime
import paramiko
from scp import SCPClient

now = datetime.now()
# dd/mm/YY-H:M:S
dt_string = now.strftime("%d%m%Y%H%M%S")
print("date and time =", dt_string)


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient('34.107.41.88', 22, 'test_user', 'test_password')
scp = SCPClient(ssh.get_transport())
scp.put('testResults/log.html',  recursive='True'  '/home/test_user/Kalynchuk/'+dt_string+'/log.html')


# ssh = SSHClient()
# ssh.load_system_host_keys()
# ssh.connect(hostname='34.107.41.88', 
#             username='test_user',
#             password='test_password')

# # SCPCLient takes a paramiko transport as its only argument
# scp = SCPClient(ssh.get_transport())

# scp.put('testResults/log.html', '/home/Kalynchuk')
# # scp.get('file_path_on_remote_machine', 'file_path_on_local_machine')

# scp.close()