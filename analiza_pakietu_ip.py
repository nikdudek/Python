tcp = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
tcp = tcp.replace(" ", "")

print("Source port: ", int(tcp[:4], 16))
print("Destination port: ", int(tcp[4:8], 16))

if int(tcp[18:20], 16) == 6:
  print("Protocol : TCP")

  print("Source IP: ", int(tcp[24:26], 16), ".", int(tcp[26:28], 16), ".", int(tcp[28:30], 16), ".", int(tcp[30:32], 16))

  print("Destination IP: ", int(tcp[32:34], 16), ".", int(tcp[34:36], 16), ".", int(tcp[36:38], 16), ".", int(tcp[38:40], 16))
  
  print("Data: ", bytes.fromhex(tcp[40:]).decode('utf-8'))
  
elif int(tcp[18:20], 16) == 17:
  print("Protocol : UDP")
  print("Data: ", bytes.fromhex(tcp[40:]).decode('utf-8'))
