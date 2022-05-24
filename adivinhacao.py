import random
#from unittest import runner

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)

    while(1):
        nivel = int(input("Qual a difículdade?\n(1) Fácil (2) Médio (3) Difícil\n"))
            
        if(nivel == 1):
            total_de_tentativas = 20
            break
        if(nivel == 2):
            total_de_tentativas = 10
            break
        if(nivel == 3):
            total_de_tentativas = 5
            break
        else:
            print("Opção inválida!")

    rodada = 1
    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("\nDigite um número entre 1 e 100: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        
        acertou = chute == numero_secreto 
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("\nVocê acertou\nPontuação {}".format(pontos))
            break
        else:
            print("\nEROU")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print(pontos)
            if(chute > numero_secreto):
                print("Chutou muito alto irmão")
            else:
                print("Tá pouco ainda mano")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
