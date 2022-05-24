from functools import total_ordering
from operator import index
import random

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def leitura_arquivo(caminho):
    palavras = []

    with open(caminho) as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta

def escolhe_nivel(palavra_secreta):
    while(1):
        nivel = int(input("Qual a difículdade?\n(1) Fácil (2) Médio (3) Difícil\n"))
            
        if(nivel == 1):
            total_de_tentativas = 4 * len(palavra_secreta)
            break
        if(nivel == 2):
            total_de_tentativas = 3 * len(palavra_secreta)
            break
        if(nivel == 3):
            total_de_tentativas = 2 * len(palavra_secreta)
            break
        else:
            print("Opção inválida!")
    return total_de_tentativas

def marca_letra_certa(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = chute.upper()   
        index += 1 

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta).upper())
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    mensagem_abertura()

    palavra_secreta = leitura_arquivo("palavras.txt")    
    letras_acertadas = len(palavra_secreta) * ["_"]
    erros = 0

    while(1):

        chute = input("Qual a letra? ").strip()
        if(chute in palavra_secreta and chute.upper() not in letras_acertadas):
            marca_letra_certa(chute, letras_acertadas, palavra_secreta)
        else:
            desenha_forca(erros)
            erros += 1             
                
        print(letras_acertadas)
        if "_" not in letras_acertadas:
            mensagem_vencedor()
            break

        elif  erros == 7:
            mensagem_perdedor(palavra_secreta)
            break

if(__name__ == "__main__"):
    jogar()
