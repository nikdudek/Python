datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
datagram = datagram.replace(" ", "")

print(int(datagram[:4], 16))
print(int(datagram[4:8], 16))
dlugosc = int(datagram[8:12], 16)
print(dlugosc)

print(bytes.fromhex(datagram[16:]).decode('utf-8'))
