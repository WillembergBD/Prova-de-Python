'''[Questão criada por Izadora Oliveira (adaptada)] Lurdes tem um brechó e quer um programa que armazene todas as suas 
peças com seus respectivos preços, quantidade da peça e que ela possa excluir e incluir itens depois. Use uma lista ou 
lista composta para armazenar o nome do item, o preço e a quantidade. Faça um menu com opções de incluir e excluir os 
itens ( que forem vendidos). No final o programa deve mostrar os itens vendidos (excluídos), a lista com os itens 
cadastrados( apenas aqueles que não foram vendidos e o total vendido. '''

estoque = []
temp = []
venda = []
while True:
    print("1- Incluir peça no estoque")
    print("2- Vender Peça")
    op = int(input())

    if op == 1:
        while True:
            peca = (str(input("Digite o nome da peça:")))
            preco = (float(input("Digite o preço da peça:")))
            quant = (int(input("Digite a quantidade da peça:")))
            estoque.append([peca, preco, quant])
            
            op = (str(input("Deseja cadastra mais alguma peça? S/N ")))
            if op in 'Nn':
                break

    if op == 2:
        if estoque == 0:
            print("Nenhuma peça cadastrada")
        
        print("-="*20)
        print(f'{"Nº":<4}{"Peça":<10}{"Preço":<10}{"Quantidade":<10}')
        for i, a in enumerate(estoque):
            print(f'{i:<4}{a[0]:<10}{a[1]:<10}{a[2]:<10}')
        print("-="*20)

        while True:
            op = (int(input("Digite o número da peça que deseja vender:")))
            if op <= len(estoque) -1:
                venda.append(estoque[op])
                estoque.remove(estoque[op])
            op = (str(input("Deseja vender mais alguma peça? S/N ")))
            if op in 'Nn':
                break
                

    op = (str(input("Deseja sair do sistema? S/N ")))
    if op in 'Ss':
        break


print("-="*20)
print("           Peças Vendidas             ")
print(f'{"Nº":<4}{"Peça":<10}{"Preço":<10}{"Quantidade":<10}')
for i, a in enumerate(venda):
    print(f'{i:<4}{a[0]:<10}{a[1]:<10}{a[2]:<10}')
print("-="*20)

print("-="*20)
print("     Peças Cadastradas que não foram Vendidas        ")
print(f'{"Nº":<4}{"Peça":<10}{"Preço":<10}{"Quantidade":<10}')
for i, a in enumerate(estoque):
    print(f'{i:<4}{a[0]:<10}{a[1]:<10}{a[2]:<10}')
print("-="*20)