## Nada obstante a matéria ministrada em sala de aula, focar em resolução de problemas através da lingaguem JavaScript, o professor propõs exercício de nivelamento em Python para aferir a capacidade técnica da turma.

maiorAltura = float('-inf')
somaAlturaHomens = 0
mediaHomens = 0
menorAltura = float('inf')
quantidadeMulheres = 0
quantidadeHomens = 0

for nivelamento in range(16):
    altura = float(input('Digite sua altura: '))
    genero = input('Digite seu gênero(M/F): ').upper()

    maiorAltura = max(maiorAltura,altura)
    menorAltura = min(menorAltura,altura)

    if genero == 'M':
      somaAlturaHomens += altura
      quantidadeHomens += 1
    elif genero == 'F':
      quantidadeMulheres +=1
    mediaHomens = somaAlturaHomens / (15 - quantidadeMulheres)

print(f'Maior altura: , {maiorAltura}')
print(f'Menor altura: , {menorAltura}')
print(f'Quantidade de mulheres: {quantidadeMulheres}')
print(f'Quantidade de homens: {quantidadeHomens}')
print(f'Média de altura dos homens: , {mediaHomens}')