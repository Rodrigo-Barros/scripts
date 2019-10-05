#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#anexo
from email import encoders
from email.mime.base import MIMEBase
import os
import mimetypes

#email = "rodrigogenio12@gmail.com"
email = "rodrigogcbarros@gmail.com"
secure_port = 587
destinatarios=open('destinatarios.txt','r')
token='ycbiddwmtlmfgmfg'
nome_do_anexo='Rodrigo_Gabriel_Clemente_de_Barros_Currículo.pdf'

content_message='Olá me chamo Rodrigo e estou procurando uma oportunidade de trabalho, por favor olhe as minhas atribuições no currículo anexo a esta mensagem.'
print('email: %s' % email)
try:
    for destinatario in destinatarios:
        msg = MIMEMultipart()
        msg["Subject"] = "Currículo | Rodrigo Barros"
        msg["From"] = "Rodrigo Barros <rodrigogcbarros@gmail.com>"
        msg["To"] = destinatario
        msg.attach(MIMEText(content_message, 'plain','utf-8'))

        #anexo
        anexo='/home/rodrigo/Documentos/Educação/CV_DEV.pdf'
        ctype, encoding = mimetypes.guess_type(anexo)

        maintype, subtype = ctype.split('/', 1)
        mime = MIMEBase(maintype, subtype)
        f=open(anexo,'rb')
        mime = MIMEBase(maintype, subtype)
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', 'attachment', filename=nome_do_anexo)
        msg.attach(mime)

        #adiciona_anexo(msg,'/home/rodrigo/Desktop/Rodrigo_Gabriel_Clemente_de_Barros_Currículo.pdf')

        email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        email_server.login(email, token)
        email_server.sendmail(email, destinatario, msg.as_string())
        email_server.close()
        print("Email enviado com sucesso para o destinario %s" % destinatario)
except KeyboardInterrupt:
    print("\nabortando...")
except Exception as e:
    print(e)
