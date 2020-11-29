import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', 8080))
serv.listen(5)



conn, addr = serv.accept()
from_client = ''
while True:
  data = conn.recv(4096)
  decoded = data.decode('utf8')
  data_type, value = decoded.split(':')
  print('Type: {}, Value: {}'.format(data_type, value))

conn.close()

