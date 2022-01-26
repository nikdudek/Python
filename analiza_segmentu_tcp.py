tcp = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
tcp = tcp.replace(" ", "")

print(int(tcp[:4], 16))
print(int(tcp[4:8], 16))
dlugosc = int(tcp[24], 16)

print(bytes.fromhex(tcp[dlugosc*8:]).decode('utf-8'))
