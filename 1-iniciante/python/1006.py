# Problema 1006 - Média 2 @ Beecrowd
# Leitura e armazenamento de 3 valores de ponto flutuante, a, b e c.
a=float(input())
b=float(input())
c=float(input())
# Cálculo de média com variáveis possuindo pesos distintos.
media=((a*2)+(b*3)+(c*5))/10
# Impressão do resultado armazenado em media com formatação para que apresente 1 casa decimal após o ponto.
print(f"MEDIA = {media:.1f}")
# Codificado e disponibilizado por Emanuel Guedes