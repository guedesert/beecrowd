# Problema 1010 - Cálculo Simples @ Beecrowd
# Leitura e armazenamento de 2 strings contendo o código, a quantidade e o valor unitário de cada peça separados apenas por um espaço, que será transformado em uma lista com o método split().
peca1=input().split(" ")
peca2=input().split(" ")
# Criação e atribuição dos valores contidos nas listas peca1 e peca2 para variáveis que representarão o código, a quantidade e o valor unitário de cada peça baseadas no índice das listas peca1 e peca2.
c1,q1,v1=peca1
c2,q2,v2=peca2
# Cálculo e atribuição de valores dos totais de cada peça considerando quantidade como um valor inteiro e valor unitário como um valor de ponto fluante, visto que, até o momento, eram strings, sendo necessária a conversão de tipo de dados.
t1,t2=int(q1)*float(v1),int(q2)*float(v2)
# Soma e atribuição dos valores de referentes ao total obtido de cada peça.
total=t1+t2
# Impressão do resultado armazenado na variável total com precisão de 2 casas decimais depois do ponto.
print(f"VALOR A PAGAR: R$ {total:.2f}")
# Codificado e disponibilizado por Emanuel Guedes