# Problema 1035 - Teste de Seleção 1 @ Beecrowd
# Leitura e armazenamento de 4 valores inteiros separados por um espaço em branco.
a,b,c,d = (int(valor) for valor in input().split(" "))
# Verificação múltipla dos parâmetros considerados válidos segundo à questão utilizando o operador and() e, após a verificação, se o resultado for verdadeiro, realiza a impressão da frase "Valores aceitos".
if ((b>c)and(d>a)and((c+d)>(a+b))and((c>=0)and(d>=0))and(a%2==0)):
          print("Valores aceitos")
# Caso a verificação anterior retorne falso, será feita a impressão da frase "Valores nao aceitos".
else:
  print("Valores nao aceitos")
# Codificado e disponibilizado por Emanuel Guedes