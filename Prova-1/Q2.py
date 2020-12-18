'''[Questão criada por Nicolas Mathias (adaptada)] Cinco amigos saíram para jantar fora e nessa noite ficou definido 
que seria feito um sorteio para quem iria pagar a conta. Para isso faça um dicionário com os nomes dos amigos, 
faça um sorteio dentre esses para ver quem vai pagar a conta. Além disso, seu programa deve pegar o valor da conta 
que pode ser adiciono os 10% do garçom. '''

import random
nomes = {}
contatotal = 0 

print('-'*15, 'SORTEIO', "-"*15)

print("Digite os nomes dos 5 amigos")
for a in range(5):
    nomes[a] = str(input("Nome:"))

conta = float(input("Informe o valor da conta:"))
op = str(input("Deseja pagar os 10% do garcom? S/N"))

if op in 'Ss':
    conta = conta + conta*0.10
    sorteado = random.choice(list(nomes.values()))
    print(f'{sorteado} Vai ter que pagar a conta de {conta}R$, mas parabéns pela educação e pagar os 10% do garçom')

if op in 'Nn':
    sorteado = random.choice(list(nomes.values()))
    print(f'{sorteado} Vai ter que pagar a conta de {conta}R$, mas da próxima paga os 10% do garçom tambem.')

