# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: João Nogueira Roxo da Fonseca, johnroxo@hotmail.com
# - aluno B: Gabriela Choichit Giosa, gabichoichit@gmail.com
#essa linha eh apenas um teste
from random import randint
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual['titulo'])
        print(len(cenario_atual['titulo'])*'-')
        print(cenario_atual['descricao'])
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Suas opcoes:")
            for x,y in opcoes.items():
                print ("{0}:{1}".format(x,y))
            escolha = input('qual sua opcao?')

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")
# função feature 1
x = randint(1,2)
s = 0
if x == 1:
    print("Você encontrou um monstro")
    y = input("O que quer fazer? lutar ou correr?")
    if y == ("lutar"):
         print("Você morreu!")
    else:
        print("Você voltou ao saguão principal"
              "O que quer fazer?")
else:
    print("Parabéns!!Você ganhou um prêmio de 100$")
    s += 100
# Programa principal.
if __name__ == "__main__":
    main()
    

#import random
#
#print("Você encontrou um monstro, Agora terá que lutar pela sua vida!")
#
#playerslife = 100
#monstro = 100
#
#while playerslife >0 and monstro >0:
#    x = random.randint(1,2)
#    if x == 1: 
#        print("Ataque efetivo, menos 20 pontos para o monstro")
#        monstro -= 20
#    else:
#        print("Lesou e o monstro te deu um soco, perdeu 20 pontos de vida")
#        playerslife -= 20
#        
#if playerslife < 0:
#    print("você morreu!")
#
#
#else:
#    print("voce ganhou! O resto do trajeto ate o Insper foi tranquilo!") 
 
