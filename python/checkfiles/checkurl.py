# -*- coding: utf-8 -*-

import os
from termcolor import colored

response=os.system("python pythonExecption.py")
if response == 0:
    print (colored("[Ok]","white","on_green")+" não foram encontrados erros de dependência em seu código")
else:
    exit(1)
