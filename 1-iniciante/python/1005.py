# Problema 1005 - Média 1 @ Beecrowd
# Leitura e armazenamento de 2 valores de ponto flutuante, a e b.
a=float(input())
b=float(input())
# Cálculo de média com variáveis possuindo pesos distintos.
media=((a*3.5)+(b*7.5))/11
# Impressão do resultado armazenado em media com formatação para que apresente 5 casas decimais após o ponto.
print(f"MEDIA = {media:.5f}")
# Codificado e disponibilizado por Emanuel Guedes