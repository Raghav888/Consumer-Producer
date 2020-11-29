import socket
import random
import time


import string

def random_number():
	return str(random.randint(0, 100))
	

def random_string():
        return ''.join([random.choice(string.ascii_lowercase) for i in range(random.randint(0, 20))])
        
def random_float():
        return str(random.random())


def random_message():
        generators = {
                'NUMBER': random_number,
                'STRING': random_string,
                'DOUBLE': random_float
        }
        
        generator_type = random.choice(list(generators.keys()))
        return generator_type + ':' + generators[generator_type]()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('server', 8080))



while True:
      message=random_message()
      raw_message=bytes(message, 'utf8')
      client.send(raw_message)
      time.sleep(1)
client.close()

