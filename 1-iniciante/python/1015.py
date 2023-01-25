# Problema 1015 - Distância Entre Dois Pontos @ Beecrowd
# Importa a biblioteca math, que contém o método que calcula a raiz quadrada.
import math
# Lê e armazena os números nas variável p1, como lista, mas antes separando os números a partir do método split() e convertando o tipo para decimal com o método float().
p1 = [float(n) for n in input().split(" ")]
# Lê e armazena os números nas variável p2, como lista, mas antes separando os números a partir do método split() e convertando o tipo para decimal com o método float().
p2 = [float(n) for n in input().split(" ")]
# Calcula a distancia entre os pontos contidos nas 2 listas considerando p2 como o ponto final e p1 como o inicial e sendo o índice 0 referente ao x e 1 referente ao y.
distancia = math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
# Imprime o resultado com precisão de 4 casas após o ponto decimal.
print(f"{distancia:.4f}")
# Codificado e disponibilizado por Emanuel Guedes