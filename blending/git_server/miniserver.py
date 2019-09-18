import os
from time import sleep
os.system('./server.sh')
os.system('disown')
sleep(10)
print('hello world')
