# -*- coding: utf-8 -*-

import os

response=os.system("python pythonExecption.py")
if response == 0:
    print ("não foram encontrados erros de dependencia em seu codigo")
else:
    exit(1)
