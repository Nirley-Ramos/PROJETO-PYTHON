real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.48
euro = real / 5.92
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))