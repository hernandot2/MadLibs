
status = int(input("Qual seu codigo de status(1-4): "))
qty_wallets = input("qty wallets: ") 


if ((status == 1 and  qty_wallets > 1) or (status == 2 and  qty_wallets > 2) or (status == 3 or status == 4) and  qty_wallets > 3)):
  print(" voce tera que pagar uma taxa de servico por excesso de bagagem!")
else:
  comprimento = int(input( "comprimento(cm): "))
  largura = int(input("largura(cm): "))
  altura = int(input("altura(cm): "))
  peso  = int(input("peso(kg): "))

  if ( comprimento + largura + altura + peso )


3- qtd de malas > 4
4- elif ou else - informar largura, altura, peso 
5- Caso contrario print(" Tudo ok com as bagagens, tenha uma boa viagem")



input