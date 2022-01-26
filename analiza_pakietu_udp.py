tcp = "68 00 55 6f 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
tcp = tcp.replace(" ", "")

print("Source port: ", int(tcp[:4], 16))
print("Destination port: ", int(tcp[4:8], 16))

print("Data: ", bytes.fromhex(tcp[16:]).decode('utf-8'))
