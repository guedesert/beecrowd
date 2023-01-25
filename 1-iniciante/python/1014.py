# Problema 1013 - O Maior @ Beecrowd
# Lê e armazena o valor inteiro relativo à distância total.
distancia = int(input())
# Lê e armazena o valor decimal relativo ao combustível gasto.
combustivel = float(input())
# Calcula o consumo considerando que equivale a distância total dividida pelo combustível gasto, para descobrir quantos km o veículo consegue fazer com 1 L de combustível.
consumo = distancia/combustivel
# Imprime o resultado.
print(f"{consumo:.3f} km/l")
# Codificado e disponibilizado por Emanuel Guedes