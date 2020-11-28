import socket
import random
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))


while True:
      num=(random.randint(0,100))
      num=bytes(num)
      client.send(num)
      time.sleep(1)
client.close()

