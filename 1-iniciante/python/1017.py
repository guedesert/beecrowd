# Problema 1017 - Gasto de Combustível @ Beecrowd
# Lê e armazena o número inteiro referente ao tempo.
tempo = int(input())
# Lê e armazena o número inteiro referente à velocidade.
velocidade = int(input())
# Calcula a quantidade de litros de combustível gastos considerando a velocidade e o tempo de percurso.
combustivel = velocidade*tempo/12
# Imprime a quantidade de litros de combustível gastos.
print(f"{combustivel:.3f}")
# Codificado e disponibilizado por Emanuel Guedes