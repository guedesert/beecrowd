# Problema 1018 - Cédulas @ Beecrowd
# Lê e armazena um valor inteiro.
valor = int(input())
# Copia o valor entrado para c1, que é a quantidade de cédulas de R$ 1,00, que será usado para os cálculos de quantidade de cédulas, pois o valor original será usado na impressão final.
c1 = valor
# Calcula a quantidade de cédulas de R$ 100,00 podem ter no valor informado fazendo uma divisão exata por 100.
c100 = c1//100
# Armazena o resto da divisão de c1 por 100 em c1.
c1 %= 100
# Calcula a quantidade de cédulas de R$ 50,00 podem ter no valor informado fazendo uma divisão exata por 50.
c50 = c1//50
# Armazena o resto da divisão de c1 por 50 em c1.
c1 %= 50
# Calcula a quantidade de cédulas de R$ 20,00 podem ter no valor informado fazendo uma divisão exata por 20.
c20 = c1//20
# Armazena o resto da divisão de c1 por 20 em c1.
c1 %= 20
# Calcula a quantidade de cédulas de R$ 10,00 podem ter no valor informado fazendo uma divisão exata por 10.
c10 = c1//10
# Armazena o resto da divisão de c1 por 20 em c1.
c1 %= 10
# Calcula a quantidade de cédulas de R$ 5,00 podem ter no valor informado fazendo uma divisão exata por 5.
c5 = c1//5
# Armazena o resto da divisão de c1 por 5 em c1.
c1 %= 5
# Calcula a quantidade de cédulas de R$ 2,00 podem ter no valor informado fazendo uma divisão exata por 2.
c2 = c1//2
# Armazena o resto da divisão de c1 por 2 em c1, resultando na quantidade de cédulas de R$ 1,00.
c1 %= 2
# Impressão do resultado contendo o valor informado inicialmente e as quantidades de cada cédula separados por uma quebra de linha feita com "\n".
print(f"{valor}\n{c100} nota(s) de R$ 100,00\n{c50} nota(s) de R$ 50,00\n{c20} nota(s) de R$ 20,00\n{c10} nota(s) de R$ 10,00\n{c5} nota(s) de R$ 5,00\n{c2} nota(s) de R$ 2,00\n{c1} nota(s) de R$ 1,00")
# Codificado e disponibilizado por Emanuel Guedes