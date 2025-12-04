import socket
import struct

HOST = "vortex.labs.overthewire.org"
PORT = 5842
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

sum = 0
for i in range(0,4):
        data = s.recv(4)
        print(f"Raw bytes: {data}")

        number = struct.unpack("<I", data)[0]
        print(f"As integer: {number}")
        sum += number

print(f"\nFinal sum: {sum}")
s.send(struct.pack("<I",sum))

response = s.recv(1024)
print(f"Server response: {response}")
