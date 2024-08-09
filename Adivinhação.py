#Colocando os módulos e declarando as váriaveis
import random
import time
número_Aleatorio = random.randint(0,100)
tentativas = 0
acertou = False
#Fazendo a introdução do jogo ao jogador
print('Bem vindo ao Jogo de adivinhação em python')
time.sleep(1)
nome = str(input('Me diga qual seu nome?: '))
print(f'Okay {nome} Vamos ver se consegue adivinhar \nO número que eu pensei entre 0 e 100')
#Sistema Para Checar o Palpite do Jogador
while not acertou:
    time.sleep(1)
    palpite = int(input('Digite seu Palpite: '))
    tentativas+=1
    if palpite == número_Aleatorio:
        acertou = True
        print(f'Parabéns {nome} você acertou o número em {tentativas} tentativas')
    #Sistema para auxiliar o jogador a chegar no número
    elif palpite < número_Aleatorio:
        print('O número que pensei é maior tente denovo')
    else:
        print('O número que pensei é menor tente denovo')

