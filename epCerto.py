# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: João Nogueira Roxo da Fonseca, johnroxo@hotmail.com
# - aluno B: Gabriela Choichit Giosa, gabichoichit@gmail.com
#essa linha eh apenas um teste
import random 


def carregar_cenarios():
    cenarios =  {
        "saguao insper": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "carona": {
            "titulo": "Caroninha do seu Jurandir",
            "descricao": "A kombi do seu Jurandir te deixou com sucesso na porta do Insper",
            "opcoes":{
                "saguao insper": "Entrar no insper.",
                "predio 2": "Ir para o predio 2 para tentar fazer o EP.",
            }
        },
        "onibus": {
            "titulo": "Busao para SP",
            "descricao" : "Voce pegou um onibos para Sp, porem apareceu um monstro no seu Busao.",
            "opcoes":{
                "lutar busao" : "tentar lutar contra o monstrengo(voce so tem essa opcao.).",
            }
        },
        "predio 2": {
            "titulo": "Voce foi para o predio 2.",
            "descricao" : "Voce nao conseguiu fazer o EP a tempo",
            "opcoes" : {}
        },
                        
        "charrete": {
            "titulo": "Simples mais eficiente",
            "descricao": "O cavalo ficou desidratado e desmaiou.",
            "opcoes": {
                "onibus": "Voltar para sua RP e pegar um onibus.",
                "carona": "Pegar carona com seu Jurandir e sua kombi.",
            }
        },
        "luta": {
            "titulo": "luta",
            "descricao": "voce saiu na porrada com o monstro",
            #luta(if ganha opcoes, perde game over)
            "opcoes": {
                "saguao insper" : " Ir para entrada do Insper.",
            }
        } ,                              
        "casa":{
            "titulo": "Cidade Raiz",
            "descricao": "Voce esta em Ribeirao Preto (Terra do cafe) em sua casa.",
            "opcoes":{
                "onibus": "Pegar um onibus direto para Sao Paulo",
                "charrete" : "Ir de charrete para Sao Paulo"
            }
        },
            
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "saguao insper": "Tomar o elevador para o saguao de entrada",
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
                "saguao insper": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "casa"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("Falta 1 dia para entrega do EP! Você está "
        "na sua casa, e precisa decidir como vai para Sao Paulo. "
        )
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        if cenario_atual == 'luta':
            
            
        
        print(cenario_atual['titulo'])
        print(len(cenario_atual['titulo'])*'-')
        print(cenario_atual['descricao'])
        opcoes = cenario_atual['opcoes']
            import random
            inventario = ["gema da vida"]

            print("Você encontrou um monstro, Agora terá que lutar pela sua vida!")
            jogador = 100
            monstro = 100

            print("A luta começou")
            while jogador > 0 and monstro > 0:
                A = int(input("Escolha um numero de 0 a 10: "))
                B = random.randint(1,10)
                if A == B:
                    ataque_player = 20
                else:
                    ataque_player = random.randint(15,19)
                    x = random.randint(1,3)
                    if x <= 2:
                        monstro -= ataque_player
                        print("O ataque que você deu foi efetivo:")
                        print(ataque_player)
                        print("a vida do monstro agora é igual a:")
                        print(monstro)
                    else:
                        jogador -= 10
                        print("O monstro te atingiu, sua vida agora é igual a:")
                        print(jogador)
        
            if jogador <=0:
                print("Você morreu!")
            else:
                print("Voce ganhou, parabens!!Sua vida agora é igual a:")
                print(jogador)
                print("Após a luta mais acirrada da sua vida, você derrotou o monstro, parabens!!")
                y = random.randint(1,100)
                if y <= 25:
                    if "gema de teleporte" not in inventario:
                        inventario.append("gema de teleporte")
                elif y > 25  and y <= 50:
                    if "gema de vida" not in inventario:
                        inventario.append("gema de vida")
                elif y < 50 and y > 75:
                    if "gema de ataque" not in inventario:
                        inventario.append("gema de ataque")
                elif y > 75 and y <= 99:
                    print("Porem não ganhou nada, siga a sua jornada!")
                else:
                    if "gema de EP feita" not in inventario:
                        inventario.append("gema de EP feita")
                        print("Parabens!! Voce ganhou a gema de EP concluida, ela torna a sua EP feita e perfeita!Va até o professor e faça a entrega")
                        print("Este é o seu inventario após a batalha:")
                        print(inventario)
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
           

    print("Você perdeu!")



# Programa principal.
if __name__ == "__main__":
    main()
    




