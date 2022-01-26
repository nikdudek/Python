import socket, base64

def response():
    response = b''
    while not b'\r\n' in response:
        response += s.recv(2048)
    print(str(response))
    print('\n')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('poczta.interia.pl', 587))
response()


#EHLO
msg = 'EHLO Dom\r\n'
s.sendall(msg.encode('utf-8'))
response()

#AUTH LOGIN
msg = 'AUTH LOGIN\r\n'
s.sendall(msg.encode())
response()

#LOGIN & PASS
crlmsg = '\r\n'
user = base64.b64encode('domi.du@interia.pl'.encode())
pasw = base64.b64encode('xsw2!QAZ'.encode())

s.sendall(user)
s.sendall(crlmsg.encode())
response()


s.sendall(pasw)
s.sendall(crlmsg.encode())
response()

#MAIL FROM
msg = 'MAIL FROM: <pas.2018@interia.pl>\r\n'
s.sendall(msg.encode())
response()

#RCPT TO
msg = 'RCPT TO: <dxdspensin@gmail.com>\r\n'
s.sendall(msg.encode())
response()

#DATA
msg = 'DATA\r\n'
s.sendall(msg.encode())
response()

#MAIL
mail = '''Content-Type: multipart/mixed; boundary =\"separator\"
MIME-Version:   1.0
To: <sth@gmail.com>
From: <sth@Interia.pl>
Subject: Wiadomosc testowa
--separator
Content-Type: text/plain; charset=\" us-ascii\"
Wiadomosc testowa.
--separator
ContentType: application/octet-stream; Name=\"wiadomosc\"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename=\"wiadomosc.txt\"
    
'''

s.sendall(mail.encode())

with open("file.txt", 'r') as attachment_file:
    content = attachment_file.read()
    content_base = base64.b64encode(content.encode())
    s.sendall(content_base)

end = '''
--separator--'''

s.sendall(end.encode())
s.sendall("\r\n.\r\n".encode('ascii'))
response()

#QUIT
msg = 'QUIT\r\n'
s.sendall(msg.encode())
response()
s.close()
