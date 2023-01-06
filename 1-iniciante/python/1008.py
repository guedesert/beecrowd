# Problema 1008 - Salário @ Beecrowd
# Leitura e armazenamento do número que representa o funcionário.
func=int(input())
# Leitura e armazenamento do número de horas trabalhadas pelo funcionário.
numhoras=int(input())
# Leitura e armazenamento do valor, em ponto flutuante, do valor da hora trabalhada.
valhora=float(input())
# Cálculo e armazenamento do valor do salário.
salario=numhoras*valhora
# Impressão do número do funcionário e do valor do salário a receber, com precisão de 2 casas decimais depois do ponto.
print(f"NUMBER = {func}\nSALARY = U$ {salario:.2f}")
# Codificado e disponibilizado por Emanuel Guedes