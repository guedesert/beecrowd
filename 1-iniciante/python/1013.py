# Problema 1013 - O Maior @ Beecrowd
# Lê e armazena os 3 números nas variáveis a, b e c, mas antes separando os números a partir do método split(), convertando o tipo para inteiro com o método int() e organizando os números, de forma crescente, portanto, o maior sempre ficará armazenado em c e o menor em a.
a,b,c = sorted(int(n) for n in input().split(" "))
# Impressão no número na variável c, que contém o maior número entre os informados.
print(f"{c} eh o maior")
# Codificado e disponibilizado por Emanuel Guedes