# Problema 1013 - Área @ Beecrowd
# Lê e armazena os 3 números nas variáveis a, b e c, mas antes separando os números a partir do método split() e convertando o tipo para decimal com o método float().
a, b, c = (float(n) for n in input().split(" "))
# Criação e definição do valor de π.
pi = 3.14159
# Calcula a área do triângulo.
triangulo = (a*c)/2
# Calcula a área do círculo.
circulo = pi*(c**2)
# Calcula a área do trapézio.
trapezio = ((a+b)*c)/2
# Calcula a área do quadrado.
quadrado = b**2
# Calcula a área do retângulo.
retangulo = a*b
# Imprime os resultados com precisão de 3 casas decimais após o ponto, separando os resultados por uma quebra de linha "\n".
print(f"TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}")
# Codificado e disponibilizado por Emanuel Guedes