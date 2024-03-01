# 1

# a = int(input('Digite o primeiro número.'))
# b = int(input('Digite o segundo número.'))
#
#
# print('Dividendo', a)
# print('Divisor', b)
# print('Quociente', a/b)
# print('Resto', a%b)

# 2
# a = int(input('Digite o primeiro número.'))
# b = int(input('Digite o segundo número.'))
# c = int(input('Digite o terceiro número.'))
# d = int(input('Digite o quarto número.'))
#
# media_ponderada = (a*1 + b*2 + c*3 + d* 4 )/(1+2+3+4)
# print('A média ponderada é ', media_ponderada)

# 3
#
# nome = input('Digite um nome.')
#
# print(nome)
# print(nome[0])
# print(nome[-1])
# print(nome[0:3])
# print(nome[2])
# print(nome[3])
# print(nome[-1], nome[-2])

# 4

# valor_aula = int(input('Insira o valor da aula\n'))
# qntd_aulas = int(input('insira a quantidade de aulas dadas\n'))
# percentual_inss = float(input('Insira o percentual que será descontado. Ex: 0.05\n'))
#
# salario_base = valor_aula*qntd_aulas
# salario_final = salario_base - (percentual_inss*salario_base)
#
# print('Salario final é ', salario_final)

# 5
# consumo_do_carro = 12
# tempo_viagem = float(input('Insira o tempo total da viagem \n'))
# velocidade_media =float(input('Insira velocidade da viagem em KM/h\n'))
#
#
# #dado que velocidade é distancia/tempo
# distancia_percorrida = velocidade_media*tempo_viagem
# consumo_da_viagem = distancia_percorrida/consumo_do_carro
#
# print(f'A distancia percorrida foi de {distancia_percorrida} KM.')
# print(f'O consumo foi de {consumo_da_viagem} litros.')

# 6

# valor = float(input('Agiota: Quanto dinheiro voce quer?\n'))
# taxa_juros = float(input('Agiota: Você aceita uma taxa de juros de quanto? Ex: 0.10\n'))
# meses = int(input('Agiota: Vai me pagar em quantos meses???'))
#
# valor_parcela =(valor + (taxa_juros*valor)) /meses
#
# print(f'Agiota: Beleza, quero todo mês {valor_parcela} reais na minha conta! E é melhor pagar direitinho...')



#7
# qntd_fitas = int(input('Digite quantas fitas existem na locadora \n'))
#
# valor_fita = float(input('Digite o valor unitário da fita \n'))
#
# faturamento_anual = (valor_fita*(qntd_fitas*1/3)) *12
# print(f'Faturamento anual: {faturamento_anual}')
#
#
# valor_multa =0.10
# qntd_fitas_atrasam_mensalmente = (qntd_fitas*1/3*0.10)
# faturamento_mensal_multas = valor_multa*valor_fita*qntd_fitas_atrasam_mensalmente
# print('Faturamento mensal com multas:', faturamento_mensal_multas)
#
# qntd_fitas_perdidas = 0.02*qntd_fitas
# qntd_fitas_compradas = 0.10*qntd_fitas
#
# qntd_fitas_final_ano = qntd_fitas - qntd_fitas_perdidas + qntd_fitas_compradas
# print('Quantidade de fitas ao final do ano: ', qntd_fitas_final_ano)

#8

# num_conta = int(input('DIgite o numero da conta'))
# cent = num_conta//100
# dez = (num_conta %100)//10
# uni = (num_conta%10)
# inverso = uni *100 + dez * 10 + cent
#
# soma = num_conta+inverso
#
# cent_soma = soma//100
# dez_soma = (soma %100)//10
# uni_soma = (soma%10)
# print(inverso)
#
# soma_dos_produtos_pela_posicao = cent_soma* 1 + dez_soma *2 + uni_soma* 3
# print(soma_dos_produtos_pela_posicao)
# digito_verificador = soma_dos_produtos_pela_posicao%10
#
# print(f'Seu digito verificador é {digito_verificador}')

# 9
# frase = input("Digite uma frase qualquer")
# saida = ''
# cont = len(frase) - 1
#
# while cont >= 0:
#     saida = saida + frase[cont]
#     cont -= 1
# print(saida)

#10
frase = 'Python é muito legal'
palavras = frase.split()

print(f'Tamanho frase: {len(frase)} \n')

print('Tamanho de cada palavra:')
for palavra in palavras:
    print(len(palavra))
