import urllib.request

pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
texto  = pagina.read().decode("utf8")
print(texto)

pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
texto = pagina.read().decode("utf8")
inicio = texto.find(">$") + 2
fim = texto.find('</', inicio)
preco = texto[inicio:fim]
print (preco)


pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
texto  = pagina.read().decode("utf8")
onde  =  texto.find(">$")
inicio  = onde + 2
fim  = inicio + 4
preco  = texto[inicio:fim]
preco = float(preco)
print (preco)
preco1= str(preco)

if preco <= 4.70:
    print('Comprar! Preço:' + preco1)
else:
    print('Espere! Preço:' + preco1)


import smtplib


def email():
  destino = input('insira seu email:')
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login("ribeiroluiza.jlle@gmail.com", "jkgjzegsctmcfkra")
  server.sendmail(
    "ribeiroluiza.jlle@gmail.com",
    destino,
    "compra o cafe, ta barato")
  

if preco <= 4.70:
  email()
  print('email enviado')
else:
  print('preço alto, email não enviado')
