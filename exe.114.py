import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLErro:
    print('O site não esta acessivel no momento')
else:
    print('Consegui acessar o site com sucesso!')


