# Problema 1009 - Salário com Bônus @ Beecrowd
# Leitura e armazenamento do nome do vendedor.
vendedor=input()
# Leitura e armazenamento do valor do salário, em ponto flutuante.
salario=float(input())
# Leitura e armazenamento do valor das vendas realizadas, em ponto flutuante.
vendas=float(input())
# Cálculo e armazenamento do valor da comissão, 15% sobre o valor das vendas.
comissao=vendas*0.15
# Cálculo e armazenamento do valor total a pagar ao vendedor.
total=salario+comissao
# Impressão do resultado armazenado na variável total com precisão de 2 casas decimais depois do ponto.
print(f"TOTAL = R$ {total:.2f}")
# Codificado e disponibilizado por Emanuel Guedes