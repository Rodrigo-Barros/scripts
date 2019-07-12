from googletrans import Translator
from os import popen,system
selectText=popen('xsel -o').read()
translator = Translator()
translatedText=translator.translate(selectText, dest='pt').text
system('notify-send -i dialog-information-symbolic "Tradutor" "%s"' % translatedText)

