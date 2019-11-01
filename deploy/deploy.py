
import paramiko


opts = {
    'hostname': '18.189.14.130',
    'username': 'ubuntu',
    'pkey': paramiko.RSAKey.from_private_key_file('key.pem')
}

client = paramiko.client.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(**opts)

commands = [
    'git clone https://github.com/mmatuoka/python-521'

    'sudo apt install python3-pip -y',

    'pip3 install -r python-521/requirements.txt',

    'python3 python-521/dashboard/app.py &',

]

for c in commands:
    stdin, stdout, stderr = client.exec_command(c)
    print(stdout.read().decode())

client.close()